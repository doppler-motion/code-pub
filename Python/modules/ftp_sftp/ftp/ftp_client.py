import time
import os

from ftplib import FTP
from loguru import logger
from datetime import datetime


class FtpClient:
    def __init__(self, hostname, port=21):
        self.hostname = hostname
        self.port = port
        self.username = None
        self.password = None

        self.ftp_client = FTP()
        self.file_list = []

    def login(self, username, password):
        status = 0
        try:
            self.ftp_client.set_debuglevel(0)  # 不开启调试模式

            timeout = 5
            logger.info(f"begin to connect {self.hostname} at {self.now_time()}")
            self.ftp_client.connect(self.hostname, self.port, timeout=timeout)
            logger.info(f"connect {self.hostname} success!")
            logger.info(f"begin to login {self.hostname} at {self.now_time()}")
            self.ftp_client.login(username, password)
            logger.info(f"login {self.hostname} success!")

            # 连接ftp服务器
            logger.info("ftp login info: ", self.ftp_client.welcome)  # 显示ftp登录信息
            status = 1
        except Exception as e:
            logger.warning(f"ftp connect failed, error: {e}")
        return status

    def is_same_size(self, local_file, remote_file):
        """判断远程文件和本地文件大小是否一致"""
        try:
            remote_file_size = self.ftp_client.size(remote_file)
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

    def download_file(self, local_file, remote_file):
        logger.info(f"download_file() --> local_file = {local_file} remote_file = {remote_file}")

        if self.is_same_size(local_file=local_file, remote_file=remote_file):
            logger.info(f"{local_file} have same size, no need download!")
            return
        else:
            try:
                # 设置缓冲区大小
                bufsize = 1024
                fp = open(local_file, "wb")
                self.ftp_client.retrbinary("RETR " + remote_file, fp.write, bufsize)
                fp.close()
                logger.info(f"download file >>>{remote_file}<<< success!")
            except Exception as e:
                logger.warning(f"download file go wrong, error: {e}")
                return

    def download_file_tree(self, local_path, remote_path):
        logger.info(f"download_file_tree()--->  remote_path = {remote_path} to local_path = {local_path}")
        try:
            self.ftp_client.cwd(remote_path)
        except Exception as e:
            logger.warning(f"{remote_path} not exists, ")
            return

        if not os.path.isdir(local_path):
            logger.info(f"{local_path} not exists, mkdir!")
            os.makedirs(local_path)

        logger.info(f"cd -> {self.ftp_client.pwd()}")

        # 回调清空列表
        self.file_list = []
        # 方法回调
        self.ftp_client.dir(self.get_file_list)

        remote_names = self.file_list
        for item in remote_names:
            file_type = item[0]
            file_name = item[1]
            local = os.path.join(local_path, file_name).replace("\\", "/")
            if file_type == "d":
                remote = os.path.join(self.ftp_client.pwd(), file_name).replace("\\", "/")
                logger.info(f"download_file_tree()---> download >>>{file_name}<<<")
                self.download_file_tree(local, remote)

                # 返回上层目录
                self.ftp_client.cwd("..")
                logger.info(f"return parent dir --> {self.ftp_client.pwd()}")
            elif file_type == "-":
                logger.info(f"download_file()-->  download >>>{file_name}<<<")
                self.download_file(local, file_name)

        return True

    def upload_file(self, local_file, remote_file):
        logger.info(f"upload_file()---> local_file = {local_file}, to remote_file = {remote_file}")
        try:
            if not os.path.isfile(local_file):
                logger.info(f"{local_file} not exists!")
                return

            remote_path = os.path.dirname(remote_file)
            try:
                self.ftp_client.cwd(remote_path)
            except Exception as e:
                logger.warning(f"remote path not exist! error {e}")
                self.ftp_client.rmd(remote_path)
                logger.info(f"mkdir remote path {remote_path} success!")

            if self.is_same_size(local_file=local_file, remote_file=remote_file):
                logger.info(f"[ {local_file} ] same size, no need upload!")
                return

            # 设置缓冲区大小
            bufsize = 1024
            fp = open(local_file, "rb")
            self.ftp_client.storbinary("STOR " + remote_file, fp, bufsize)
            fp.close()
            logger.info(f"upload_file() --> upload >>>{local_file}<<< success!")
        except Exception as e:
            logger.warning(f"upload file occur mistake: error: {e}")

    def upload_file_tree(self, local_path, remote_path):
        """
        上传多个文件
        :param remote_path:
        :param local_path:
        :return:
        """
        logger.info(f"upload_file_tree()---> local_path = {local_path} to remote_path = {remote_path}")
        if not os.path.isdir(local_path):
            logger.info(f"local path {local_path} not exists.")
            return

        # logger.info(f"abs path : {self.ftp_client.pwd()}")
        self.ftp_client.cwd(remote_path)
        logger.info(f"cd -> {self.ftp_client.pwd()}")

        local_name_list = os.listdir(local_path)
        logger.info(f"local file list : {local_name_list}")
        for local_name in local_name_list:
            src = os.path.join(local_path, local_name).replace("\\", "/")
            if os.path.isdir(src):
                try:
                    self.ftp_client.mkd(local_name)
                except Exception as e:
                    logger.warning(f"path exists, error: {e}")
                logger.info(f"upload_file_tree()---> upload >>> {local_name} <<<")
                self.upload_file_tree(src, local_name)
            else:
                logger.info(f"upload_file()---> upload >>> {local_name} <<<")
                self.upload_file(src, local_name)
        self.ftp_client.cwd("..")

    def close_connect(self):
        try:
            logger.info("-----> quit ftp!")
            self.ftp_client.quit()
        except Exception as e:
            logger.warning(f"quit ftp go wrong, error {e}")

    def delete_remote_file(self, remote_file):
        self.ftp_client.delete(remote_file)

    def get_file_list(self, line):
        file_arr = self.get_file_name(line)
        # 去除 . 和 ..
        if file_arr[1] not in [".", ".."]:
            self.file_list.append(file_arr)

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
    def now_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    def common_method(self):
        # print(self.ftp_client.pwd())  # 获取当前路径
        # self.ftp_client.dir("ftpDir")  # 带有详细信息的文件列表
        # print(self.ftp_client.nlst("ftpDir"))  # 获取目录下文件
        # self.ftp_client.cwd(".")  # 切换目录
        # self.ftp_client.mkd("path_name")  # 创建目录
        # self.ftp_client.delete("file_name")  # 删除文件

        file_list = []
        self.ftp_client.retrlines("LIST", file_list.append)  # cmd: MLSD, RETR, LIST, or NLST
        print("file_list:", file_list)

        # files = self.ftp_client.mlsd(path="ftpDir", facts=["type", "size", "perm"])
        # print(type(files))
        # print(files)
        # print(next(files))


def main():
    hostname = ""
    port = 0
    username = ""
    password = ""

    ftp_client = FtpClient(hostname=hostname, port=port)
    ftp_client.login(username=username, password=password)

    # ftp_client.upload_file(remote_files, os.path.join(".", "test"))  # 单个文件上传
    # ftp_client.upload_file_tree(local_path="tmp/", remote_path="ftpDir")  # 目录上传
    # ftp_client.download_file_tree(local_path="D:\\tmp\\ftp_test", remote_path="ftpDir")  # 下载目录

    # 代码中用到的细节测试
    # file_list = []
    # file_list += ftp_client.ftp_client.dir("ftpDir")
    # for file in file_list:
    #     dt = datetime.fromtimestamp(file.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    #     print(dt)

    # dir_list = []
    # ftp_client.ftp_client.dir(dir_list.append)
    # print(dir_list)

    ftp_client.close_connect()


if __name__ == "__main__":
    main()
