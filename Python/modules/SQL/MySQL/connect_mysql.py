import pymysql
import os, sys

from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB

module_path = os.path.dirname(__file__)[:os.path.dirname(__file__).index("scripts")] + "/scripts"
sys.path.append(module_path)

from common_utils.common_log import logger

# HOST = "127.0.0.1"
# PORT = 3306
# USERNAME = "root"
# PASSWORD = "123456qa!"

HOST = ""
PORT = 3306
USERNAME = "admin"
PASSWORD = ""
DB = ""

mysql_config = {
    "host": "127.0.0.1",  # MYSQL_HOST,  # "172.18.130.208",
    "port": 3306,
    "user": "root",
    "password": "",
    "db_name": ""
}


def mysql_connect():
    """
    连接数据库,获取全局禁止的规则sid
    """
    try:
        db = pymysql.connect(host=HOST,
                             user=USERNAME,
                             passwd=PASSWORD,
                             port=PORT,
                             db=DB,
                             charset="utf8")
        logger.info("连接成功！")
        return db

    except:
        logger.exception("数据库连接失败！")


def implement_mysql(sql):
    db = mysql_connect()
    cursor = db.cursor()  # 使用cursor()方法获取游标
    for i in range(1):
        try:
            cursor.execute(sql)  # 执行sql语句
            result = cursor.fetchall()
            db.commit()
            return result
        except:
            db.rollback()
            logger.exception("数据库查询失败！")
    cursor.close()
    db.close()


def get_info_mysql():
    # 建表语句
    create_sql = """create table urls (id int not null auto_increment, url varchar(1000) not null, content varchar(4000) not null, created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, primary key(id))"""

    insert_sql = """INSERT INTO urls (url, content) VALUES ("baidu.com", "this is a content.")"""

    select_sql = "select * from urls;"

    for _sql in [create_sql, insert_sql, select_sql]:
        result = implement_mysql(_sql)
        logger.info(result)


class MysqlPool:
    def __init__(self, config):
        self.POOL = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
            maxshared=3,
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            # setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            ping=0,
            host=config.get("host", "127.0.0.1"),
            port=config.get("port", 3306),
            user=config.get("user"),
            password=config.get("password"),
            database="kb_all_in_one",
            # charset='utf8'
        )

    def __new__(cls, *args, **kw):
        """
        启用单例模式
        :param args:
        :param kw:
        :return:
        """
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def connect(self):
        """
        启动连接
        :return:
        """
        try:
            conn = self.POOL.connection()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            return conn, cursor
        except Exception as e:
            logger.error(f'mysql connect error: {e}')

    @staticmethod
    def connect_close(conn, cursor):
        """
        关闭连接
        :param conn:
        :param cursor:
        :return:
        """
        try:
            cursor.close()
            conn.close()
        except Exception as e:
            logger.error(f'mysql close error: {e}')

    def fetch_all(self, sql, args=None):
        """
        批量查询
        :param sql:
        :param args:
        :return:
        """
        try:
            conn, cursor = self.connect()
            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)
            # cursor.execute(sql, args)
            record_list = cursor.fetchall()
            self.connect_close(conn, cursor)
            return record_list
        except Exception as e:
            logger.exception(f"fetchall error , sql : {sql}")
            return []

    def fetch_one(self, sql, args=None):
        """
        查询单条数据
        :param sql:
        :param args:
        :return:
        """
        try:
            conn, cursor = self.connect()
            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)
            # cursor.execute(sql, args)
            result = cursor.fetchone()
            self.connect_close(conn, cursor)
            return result
        except Exception as e:
            logger.error(f'fetchone error: {e}')

    def insert(self, sql, args=None):
        """
        插入数据
        args建议使用字典
        :param sql:
        :param args:
        :return:
        """
        conn, cursor = self.connect()
        try:
            if args:
                row = cursor.execute(sql, args)
            else:
                row = cursor.execute(sql)
            conn.commit()
        except Exception as e:
            logger.error(f'insert error: {e}')
            conn.rollback()
            row = 0
        self.connect_close(conn, cursor)
        return row

    # 增加多行
    def insertmany(self, sql, param):
        """
        :param sql:
        :param param: 必须是元组或列表[(),()]或（（），（））
        :return:
        """
        conn, cursor = self.connect()
        try:
            cursor.executemany(sql, param)
            conn.commit()
        except Exception as e:
            logger.error(f'insertmany error: {e}')
            conn.rollback()
        self.connect_close(cursor, conn)

    # 删除
    def delete(self, sql, param=None):
        conn, cursor = self.connect()
        rows = 0
        try:
            rows = cursor.execute(sql, param)
            conn.commit()
        except Exception as e:
            logger.error(f'delete error: {e}')
            conn.rollback()
        self.connect_close(cursor, conn)

        return rows

    # 更新
    def update(self, sql, args=None):
        conn, cursor = self.connect()
        row = 0
        try:
            if args:
                row = cursor.execute(sql, args)
            else:
                row = cursor.execute(sql)
            conn.commit()
        except Exception as e:
            logger.error(f'update error: {e}')
            conn.rollback()
        self.connect_close(cursor, conn)

        return row

    def execute(self, sql, args=None):
        conn, cursor = self.connect()
        row = 0
        try:
            if args:
                row = cursor.execute(sql, args)
            else:
                row = cursor.execute(sql)
            conn.commit()
        except Exception as e:
            logger.error(f'execute error: {e}')
            conn.rollback()
        self.connect_close(cursor, conn)

        return row


class BasePymysqlPool(object):
    def __init__(self, host, port, user, password, db_name=None):
        self.db_host = host
        self.db_port = int(port)
        self.user = user
        self.password = str(password)
        self.db = db_name
        self.conn = None
        self.cursor = None


class MySQLConnectPool(BasePymysqlPool):
    # 连接池对象
    __pool = None

    def __init__(self, config=None):
        super(MySQLConnectPool, self).__init__(**config)

        # 数据库构造函数，从连接池中取出连接，并生成操作游标
        self._conn = self.__get_conn()
        self._cursor = self._conn.cursor()

    def __get_conn(self):
        """
        :summary: 静态方法，从连接池中取出连接
        :return MySQLdb.connection
        """
        if MySQLConnectPool.__pool is None:
            __pool = PooledDB(creator=pymysql,
                              mincached=1,  # 启动时开启的空连接数量
                              maxcached=20,  # 连接池最大可用连接数量
                              host=self.db_host,
                              port=self.db_port,
                              user=self.user,
                              passwd=self.password,
                              db=self.db,
                              use_unicode=False,
                              charset="utf8",
                              cursorclass=DictCursor)
        return __pool.connection()

    def get_all(self, sql, param=None):
        """
        :summary: 执行查询，并取出所有结果集
        :param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        :param param: 可选参数，条件列表值（元组/列表）
        :return: result list(字典对象)/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def get_one(self, sql, param=None):
        """
        :summary: 执行查询，并取出第一条
        :param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        :param param: 可选参数，条件列表值（元组/列表）
        :return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def get_many(self, sql, num, param=None):
        """
        :summary: 执行查询，并取出num条结果
        :param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        :param num:取得的结果条数
        :param param: 可选参数，条件列表值（元组/列表）
        :return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    def insert_many(self, sql, values):
        """
        :summary: 向数据表插入多条记录
        :param sql:要插入的ＳＱＬ格式
        :param values:要插入的记录数据tuple(tuple)/list[list]
        :return: count 受影响的行数
        """
        count = self._cursor.executemany(sql, values)
        return count

    def __query(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        return count

    def update(self, sql, param=None):
        """
        :summary: 更新数据表记录
        :param sql: ＳＱＬ格式及条件，使用(%s,%s)
        :param param: 要更新的  值 tuple/list
        :return: count 受影响的行数
        """
        return self.__query(sql, param)

    def insert(self, sql, param=None):
        """
        :summary: 更新数据表记录
        :param sql: ＳＱＬ格式及条件，使用(%s,%s)
        :param param: 要更新的  值 tuple/list
        :return: count 受影响的行数
        """
        return self.__query(sql, param)

    def delete(self, sql, param=None):
        """
        :summary: 删除数据表记录
        :param sql: ＳＱＬ格式及条件，使用(%s,%s)
        :param param: 要删除的条件 值 tuple/list
        :return: count 受影响的行数
        """
        return self.__query(sql, param)

    def begin(self):
        """
        :summary: 开启事务
        """
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """
        :summary: 结束事务
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, is_end=1):
        """
        :summary: 释放连接池资源
        """
        if is_end == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()

    def execute(self, sql, param=None):
        self.__query(sql, param)


class MySQLConnect:
    def __init__(self, host, port, user, password, db_name=None):
        self.host = host
        self.port = port
        self.user_name = user
        self.password = password
        self.db_name = db_name

        self.db = None
        self.cursor = None

    def connect_msql(self):
        try:
            self.db = pymysql.connect(host=self.host,
                                      user=self.user_name,
                                      passwd=self.password,
                                      port=self.port,
                                      db=self.db_name,
                                      charset="utf8")
            # cursorclass=DictCursor)
            self.cursor = self.db.cursor()
            logger.info("connect mysql and create cursor success!")
        except:
            logger.exception("数据库连接失败！")

    def disconnect_mysql(self):
        self.cursor.close()
        self.db.close()
        logger.info("disconnect success!")

    def get_one(self, sql, column_name=None):
        result = {}
        self.connect_msql()  # 连接mysql
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            if result and column_name:
                result = dict(zip(column_name, result))
            logger.info(result)
            self.db.commit()
        except:
            logger.exception("get info failed!")
            self.db.rollback()

        finally:
            self.disconnect_mysql()

        return result

    def get_all(self, sql, column_name=None):
        result = {}
        self.connect_msql()  # 连接mysql
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            logger.info(result)
            self.db.commit()
        except:
            logger.exception("get info failed!")
            self.db.rollback()

        finally:
            self.disconnect_mysql()

        return result


if __name__ == "__main__":
    # get_info_mysql()
    mysql_connect()
