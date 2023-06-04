from clickhouse_driver import Client, connect
from loguru import logger

from clickhouse_sqlalchemy import make_session
from sqlalchemy import create_engine
import pandas as pd

# clickhouse
CLICKHOUSE_CONFIG = {
    "user": "",
    "password": "",
    "host": "127.0.0.1",
    "port": 9000,
    "database": ""
}


def restore_clickhouse_table():
    """
    清空clickhouse表
    """
    try:
        _client = Client(host=CLICKHOUSE_CONFIG.get("host"),
                         port=CLICKHOUSE_CONFIG.get("port"),
                         password=CLICKHOUSE_CONFIG.get("password"),
                         user=CLICKHOUSE_CONFIG.get("user"),
                         database=CLICKHOUSE_CONFIG.get("database"))
        # _client = Client(**CLICKHOUSE_CONFIG)
        # clickhouse_url = "clickhouse://{user}:{password}@{host}:{port}/{db}"
        # conn = connect(
        #     f'clickhouse://{CLICKHOUSE_CONFIG.get("user")}:{CLICKHOUSE_CONFIG.get("password")}@{CLICKHOUSE_CONFIG.get("host")}:{CLICKHOUSE_CONFIG.get("port")}/{CLICKHOUSE_CONFIG.get("database")}')
        # conn = connect(clickhouse_url)
        # cursor = conn.cursor()
        # _ret = _client.execute('SHOW TABLES')
        # print(_ret)

        # 清空表
        # _client.execute("""truncate table ids_abnormal_device_table_result;""")
        # _client.execute("""truncate table `all_in_one`.`ids_alert_pkg_table`;""")
        _client.execute("""truncate table `all_in_one`.`ids_protocol_flow_table`;""")
        logger.info("clear ids_protocol_flow_table success!")
    except:
        logger.exception("restore clickhouse table failed!")


connection = 'clickhouse://{user}:{password}@{host}:{port}/{database}'.format(**CLICKHOUSE_CONFIG)
engine = create_engine(connection, pool_size=100, pool_recycle=3600, pool_timeout=20)

sql = 'SHOW TABLES'
sql1 = """truncate table `all_in_one`.`ids_alert_pkg_table`;"""

session = make_session(engine)
cursor = session.execute(sql1)
try:
    fields = cursor._metadata.keys
    print(fields)
    print(cursor.keys())
    print(cursor.fetchall())
    # df = pd.DataFrame([dict(zip(fields, item)) for item in cursor.fetchall()])
    # print(df)
finally:
    cursor.close()
    session.close()

if __name__ == "__main__":
    restore_clickhouse_table()
