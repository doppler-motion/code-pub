import IPy
import re
from loguru import logger


def if_ip_in_segment(ip, segment):
    if ip in IPy.IP(segment):
        return True
    else:
        return False


def if_ip_legal(ip):
    is_legal = False
    try:
        if IPy.IP(ip):
            is_legal = True
    except:
        pass
    return is_legal


def is_ip(ip_addr: str):
    """
    判断是否是ip
    :param ip_addr:
    :return:
    """
    pattern = re.compile(r"(?<![\.\d])(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?![\.\d])")
    try:
        if pattern.match(ip_addr):
            return True
        else:
            return False
    except Exception as e:
        logger.warning(f"judge ip failed, error: {e}")
        return False


if __name__ == "__main__":
    # if if_ip_in_segment("172.32.53.4", "172.16.0.0/12"):
    #     print("1yes")
    # if if_ip_in_segment("192.168.51.69", "192.168.0.0/16"):
    #     print("2yes")
    # if if_ip_in_segment("192.168.51.22", "192.168.0.0/16"):
    #     print("3yes")

    if is_ip(""):
        print("shi ip")
    else:
        print("bushi ip")

    if if_ip_legal("210.29.176.0/20"):
        print("legal")
    else:
        print("illegal")
