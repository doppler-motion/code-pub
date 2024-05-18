import os
import sys

from loguru import logger

path = "/home/user/a.txt"

# 引用同一项目不同目录下的脚本里的函数
# 在代码开头添加
sys.path.append(os.pardir)

# 或者下面这种方式
currentdir = os.path.dirname(os.path.relpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(os.path.dirname(parentdir))  # parent dir

logger.info(sys.path)

# 改变所有者需要拿到实际的id
os.chown(path, uid=1002, gid=1002)  # os.chown() 方法用于更改文件所有者; uid -- 所属用户 ID, gid -- 所属用户组 ID
os.chmod(path, mode=772)  # 更改权限，根据需要填写实际的mode id

os.getcwd()  # 返回当前工作目录
os.chdir(path)  # 切换当前工作，目录
os.listdir(".")  # 返回path指定的文件夹包含的文件或文件夹的名字的列表。
os.remove(path)  # 删除文件
os.rmdir(path)  # 删除目录
os.removedirs(path)  # 递归删除目录
os.makedirs(path)  # 递归创建目录
os.mkdir(path)   # 创建目录
os.getpid()  # 返回当前进程的ID

os.stat(path)   # 返回值结构
                # st_mode: inode 保护模式
                # st_ino: inode 节点号。
                # st_dev: inode 驻留的设备。
                # st_nlink: inode 的链接数。
                # st_uid: 所有者的用户ID。
                # st_gid: 所有者的组ID。
                # st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
                # st_atime: 上次访问的时间。
                # st_mtime: 最后一次修改的时间。
                # st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）




