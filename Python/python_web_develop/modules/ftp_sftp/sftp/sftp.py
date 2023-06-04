import paramiko
import paramiko.util
import time
import os

from datetime import datetime
from loguru import logger


class SftpClient:
    def __init__(self, hostname, port=22):
        self.hostname = hostname
        self.port = port
        self.timeout = 10
        self.username = None
        self.password = None
        self.keyFile = None

        self.sftpClient = None
        self.sf = None
        self.file_list = []

    def login(self, username, password):
        self.username = username
        self.password = password
        status = 0
        try:
            # 获取Transport会话实例
            logger.info(f"begin to connect to {self.hostname}")
            transport = paramiko.Transport((self.hostname, self.port))
            logger.info(f"connect to {self.hostname} success!")
            transport.banner_timeout = self.timeout
            logger.info(f"begin to login {self.hostname}")
            transport.connect(username=username, password=password)
            self.sf = transport
            logger.info(f"login {self.hostname} success!")
            status = 1
            self.sftpClient = paramiko.SFTPClient.from_transport(transport)
        except Exception as e:
            logger.warning(f"connect sftp failed, error: {e}")
        return status

    def close_connect(self):
        try:
            logger.info("sftp connect close!")
            self.sf.close()
        except Exception as e:
            logger.warning(f"sftp close go wrong, error : {e}")
            pass

    def is_same_size(self, local_file, remote_file):
        """判断远程文件和本地文件大小是否一致"""
        try:
            file_info = self.sftpClient.stat(remote_file)
            remote_file_size = file_info.st_size
        except Exception as ex:
            remote_file_size = -1

        try:
            local_file_size = os.path.getsize(local_file)
        except Exception as ex:
            local_file_size = -1

        logger.info(f"local_file_size: {local_file_size},  remote_file_size: {remote_file_size}")

        if remote_file_size == local_file_size:
            return 1
        else:
            return 0

    def upload_file(self, local_file, remote_file):
        logger.info(f"upload_file()---> local_file = {local_file}, to remote_file = {remote_file}")
        try:
            if not os.path.isfile(local_file):
                logger.info(f"{local_file} not exists!")
                return

            remote_path = os.path.dirname(remote_file)
            try:
                self.sftpClient.chdir(remote_path)
            except Exception as e:
                logger.warning(f"remote path not exist! error {e}")
                self.sftpClient.mkdir(remote_path)
                logger.info(f"mkdir remote path {remote_path} success!")

            if self.is_same_size(local_file=local_file, remote_file=remote_file):
                logger.info(f"[ {local_file} ] same size, no need upload!")
                return

            self.sftpClient.put(local_file, remote_file)
            logger.info(f"sftp put local file {local_file} success!")
        except Exception as e:
            logger.warning(f"sftp put local file {local_file} failed, error: {e}")
            return

    def upload_file_tree(self, local_path, remote_path):
        logger.info(f"upload_file_tree()---> local_path = {local_path} to remote_path = {remote_path}")
        if not os.path.isdir(local_path):
            logger.info(f"local path {local_path} not exists.")
            return

        # logger.info(f"abs path : {self.sftp_client.pwd()}")
        self.sftpClient.chdir(remote_path)
        logger.info(f"cd -> {self.sftpClient.getcwd()}")

        local_name_list = os.listdir(local_path)
        logger.info(f"local file list : {local_name_list}")
        for local_name in local_name_list:
            src = os.path.join(local_path, local_name).replace("\\", "/")
            if os.path.isdir(src):
                try:
                    self.sftpClient.mkdir(local_name)
                except Exception as e:
                    logger.warning(f"path exists, error: {e}")
                logger.info(f"upload_file_tree()---> upload >>> {local_name} <<<")
                self.upload_file_tree(src, local_name)
            else:
                logger.info(f"upload_file()---> upload >>> {local_name} <<<")
                self.upload_file(src, local_name)
        self.sftpClient.cwd("..")

    def download_file(self, local_file, remote_file):
        logger.info(f"download_file() --> local_file = {local_file} remote_file = {remote_file}")
        if self.is_same_size(local_file=local_file, remote_file=remote_file):
            logger.info(f"{local_file} have same size, no need download!")
            return
        else:
            try:
                self.sftpClient.get(remote_file, local_file)
                logger.info(f"download_file() --> download >>>{local_file}<<< success!")
            except Exception as e:
                logger.info(f"download_file() --> download >>>{local_file}<<< failed, error :{e}")
                return

    def download_file_tree(self, local_path, remote_path):
        logger.info(f"download_file_tree()--->  remote_path = {remote_path} to local_path = {local_path}")
        try:
            self.sftpClient.chdir(remote_path)
        except Exception as e:
            logger.warning(f"{remote_path} not exists, error: {e}")
            return

        if not os.path.isdir(local_path):
            logger.info(f"{local_path} not exists, mkdir!")
            os.makedirs(local_path)

        logger.info(f"cd -> {self.sftpClient.getcwd()}")

        # 方法回调
        files_iter = self.sftpClient.listdir_iter()

        for file in files_iter:
            file_str = self.get_file_name(file)
            file_type = file_str[0]
            file_name = file_str[1]

            local = os.path.join(local_path, file_name).replace("\\", "/")
            remote = os.path.join(remote_path, file_name).replace("\\", "/")
            if file_type == "d":

                logger.info(f"download_file_tree()---> download >>>{file_name}<<<")
                self.download_file_tree(local, remote)

                # 返回上层目录
                self.sftpClient.chdir("..")
                logger.info(f"return parent dir --> {self.sftpClient.getcwd()}")
            elif file_type == "-":
                logger.info(f"download_file()-->  download >>>{file_name}<<<")
                self.download_file(local, file_name)

        return True

    @staticmethod
    def get_file_name(line):
        pos = line.rfind(":")
        while (line[pos] != " "):
            pos += 1
        while (line[pos] == " "):
            pos += 1
        file_arr = [line[0], line[pos:]]
        return file_arr

    @staticmethod
    def local_file_infos(line):
        file_infos = {}
        mtime = os.path.getmtime(line)
        ctime = os.path.getctime(line)
        file_name = os.path.basename(line)
        file_infos["mtime"] = mtime
        file_infos["ctime"] = ctime
        file_infos["file_name"] = file_name

        return file_infos

    @staticmethod
    def remote_file_time(line):
        file_infos = {}
        mtime = line.st_mtime
        file_name = line.filename
        file_infos["mtime"] = mtime
        file_infos["file_name"] = file_name
        return file_infos

    def time_struct(self, timestamp):
        pass

    @staticmethod
    def now_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    def delete_remote_file(self, remote_file):
        self.sftpClient.remove(remote_file)

    def file_iter(self, path):
        file_iters = self.sftpClient.listdir_iter(path)  # 获取文件迭代器
        # logger.info(type(file_iter))
        for file in file_iters:
            dt = datetime.fromtimestamp(file.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            logger.info("local time: ", dt)
            logger.info("modify time: ", file.st_mtime)  # 修改时间
            logger.info("file name: ", file.filename)  # 文件名称
            logger.info("file st_atime: ", file.st_atime)  # 访问时间
            logger.info("file longname: ", file.longname)  # 和file一样
            logger.info(file)

            # 以下暂时不知作何用
            # logger.info("file attr: ", file.attr)
            # logger.info("file st_size: ", file.st_size)
            # logger.info("file st_uid: ", file.st_uid)
            # logger.info("file st_gid: ", file.st_gid)
            # logger.info("file st_mode: ", file.st_mode)
            # logger.info("file FLAG_SIZE: ", file.FLAG_SIZE)
            # logger.info("file FLAG_UIDGID: ", file.FLAG_UIDGID)
            # logger.info("file FLAG_EXTENDED: ", file.FLAG_EXTENDED)
            # logger.info(file.__dir__())  # 输出所有的方法名
            break

    def common_method(self):
        logger.info(self.sftpClient.listdir("."))  # 查看目录下的文件
        logger.info(self.sftpClient.stat("download/sftp2.txt"))  # 查看文件的信息
        # self.sftpClient.chdir("/")  # 切换目录
        logger.info(self.sftpClient.getcwd())  # 获取当前所在目录
        # self.sftpClient.remove("")  # 删除文件
        # self.sftpClient.rmdir("")  # 删除目录
        # logger.info(self.sftpClient.__dir__())  # 查看方法

        # file_attr = self.sftpClient.listdir_attr()  # 获取目录下文件详细信息的列表
        # logger.info(type(file_attr))
        # for item in file_attr:
        #     logger.info(item)


def main():
    hostname = ""
    port = 0
    username = "sftpuser"
    password = ""

    sftp_client = SftpClient(hostname=hostname, port=port)
    sftp_client.login(username=username, password=password)

    # file_list = []
    # file_list += sftp_client.sftpClient.listdir("download/")
    # logger.info(file_list)
    # for file in file_list:
    #     if file.find(".") == -1:
    #         logger.info("is a direc")
    #     else:
    #         logger.info(file.find("."))

    # sftp_client.download_file(local_file="D:/tmp/ftp_test/aaa.txt", remote_file="/home/sftpuser/download/sftp2.txt")

    sftp_client.close_connect()


if __name__ == "__main__":
    main()
