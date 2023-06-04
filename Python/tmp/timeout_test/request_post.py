import requests


def request_url(url: str, timeout: int):
    """

    :param url:
    :param timeout:
    :return:
    """
    ret = {
        "status": 0,
        "msg": ""
    }
    try:
        response = requests.request("POST", url, timeout=timeout, verify=False)
        print(response)
        ret["status"] = 0
        ret["msg"] = "请求成功"
    except Exception as e:
        ret["status"] = -1
        ret["msg"] = "请求失败！" + str(e)

    return ret


if __name__ == "__main__":
    req_result = request_url(url="http://127.0.0.1/add_post", timeout=15)
    print(req_result)
