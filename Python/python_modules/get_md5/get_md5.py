import hashlib
import os


def string_to_md5(string):
    """
    获取字符串的MD5
    :param string:
    :return:
    """
    md5_val = hashlib.md5(string.encode("utf8")).hexdigest()
    return md5_val


def get_file_md5(file_name):
    """
    获取文件的MD5
    :param file_name:
    :return:
    """
    if not os.path.exists(file_name):
        return
    file = open(file_name, "rb")
    file_md5 = hashlib.md5(file.read()).hexdigest()
    return file_md5


url_str1 = ""

url_str2 = url_str1.format(domain="")

print(string_to_md5(url_str1))
print(string_to_md5(url_str2))
