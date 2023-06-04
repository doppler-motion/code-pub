import urllib.parse


def get_domain_by_urllib(url: str):
    """
    获取 域名
    :param url:
    :return:
    """

    return urllib.parse.urlparse(url).netloc


url_str = "a.6.7.a.5.c.a.b.b.3.6.5.7.f.6.1.0.b.7.8.e.0.4.2.9.2.1.8.9.0.4.2.ip6.arpa"

print(urllib.parse.urlparse("http://119.29.134.173:8888/sqlilabs/"))


