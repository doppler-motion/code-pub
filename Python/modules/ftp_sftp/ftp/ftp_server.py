import pyftpdlib
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter

# 记录日志输出到文件和终端
logger = logging.getLogger("FTP-LOG")
logger.setLevel(logging.DEBUG)

cs = logging.StreamHandler()
cs.setLevel(logging.INFO)

fs = logging.FileHandler(filename="test.log", mode="a", encoding="utf-8")
fs.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(asctime)s] %(name)s - %(levelname)s : %(message)s")

cs.setFormatter(formatter)
fs.setFormatter(formatter)

logger.addHandler(cs)
logger.addHandler(fs)


# 实例化虚拟用户，这是FTp的首要条件
authorizer = DummyAuthorizer()

# 添加用户权限和路径
authorizer.add_user("user", "123456", "d:/test", perm="elradfmw")

# 添加匿名用户，只需要路径
authorizer.add_anonymous("d:/test")

# 初始化ftp句柄
handler = FTPHandler
handler.authorizer = authorizer

# 上传下载的速度设置
dtp_handler = ThrottledDTPHandler
dtp_handler.read_limit = 300 * 1024  # 300 kb/s
dtp_handler.write_limit = 300 * 1024
handler.dtp_handler = dtp_handler

# 监听ip和端口，linux里需要root用户才能使用21端口
server = FTPServer(("0.0.0.0", 21), handler)

# 最大连接数
server.max_cons = 150
server.max_cons_per_ip = 15

# 开始服务，自带打印日志信息
server.serve_forever()

# 添加被动端口范围
handler.passive_ports = range(2000, 20033)

