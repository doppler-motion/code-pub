import os
import sys

from loguru import logger

path = "/home/user/test.txt"

logger.info(os.path.abspath(""))  # os.path.abspath 获取绝对路径
logger.info(os.path.dirname(path))  # os.path.dirname 去掉文件名，返回目录名 /home/user
logger.info(os.path.basename(path))  # os.path.basename 返回文件名 text.txt #
logger.info(os.path.dirname(__file__))  # /Users/ydchen/Documents/files/gitfiles/code/Python/测试脚本/modules/path
logger.info(os.path.split(path))  # os.path.split 返回(dirname, basename)元组,  ('/home/user', 'test.txt') tail: test.txt, head : /home/user # 通过一对链表的头和尾来划分路径名。链表的tail是是最后的路径名元素。head则是它前面的元素。
logger.info(os.path.split(os.path.split(path)[0]))  # ('/home', 'user') tail: user, head: /home
logger.info(os.path.splitext(path))  # os.path.splitext 分离文件名与扩展名 ('/home/user/test', '.txt')
logger.info(os.path.join("root", "user", "a.txt"))  # os.path.join, 拼接路径
logger.info(os.path.getatime("test"))  # os.path.getatime, 返回最近访问时间(浮点型秒数)
logger.info(os.path.getmtime("test"))  # os.path.getmtime, 返回最近修改时间(浮点型秒数)
logger.info(os.path.getctime("test"))  # os.path.getctime, 返回文件创建时间(浮点型秒数)
logger.info(os.path.getsize("test"))  # os.path.getsize, 返回文件大小，如果文件不存在就返回错误
# logger.info(os.path.isdir())  # os.path.isdir  	判断路径是否为目录
# logger.info(os.path.isfile())  # os.path.isfile  	判断路径是否为文件
# logger.info(os.path.normcase("\\user\\test\Ats.txt"))  # os.path.normcase(path) 转换path的大小写和斜杠

# __file__  # 当前脚本的绝对路径
logger.info(__file__)  # /Users/ydchen/Documents/files/gitfiles/code/Python/测试脚本/modules/path/path_get.py

