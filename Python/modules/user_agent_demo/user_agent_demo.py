from user_agents import parse

map_phone = {'Apple': 'Apple', 'KIW-AL10': 'Huawei', 'PRA-TL10': 'Huawei', 'PRA-AL00X': 'Huawei', 'BND-AL00': 'Huawei',
             'BND-TL10': 'Huawei', 'CAM-TL00': 'Huawei', 'BLN-AL10': 'Huawei',
             'XiaoMi': 'XiaoMi', 'MIX 2': 'XiaoMi', 'Mi Note 3': 'XiaoMi',
             'Oppo': 'Oppo', ' Oppo': 'Oppo', 'PACM00': 'Oppo', 'PBET00': 'Oppo', 'R7Plusm': 'Oppo', 'PAAT00': 'Oppo',
             'PBAM00': 'Oppo', 'PADM00': 'Oppo', 'PAFM00': 'Oppo', 'PBEM00': 'Oppo', 'PAAM00': 'Oppo', 'PBBM00': 'Oppo',
             'PACT00': 'Oppo', 'PBAT00': 'Oppo', 'PADT00': 'Oppo', 'PBBT00': ' Oppo', 'PBCM10': 'Oppo',
             'V1816A': 'vivo', 'V1732T': 'vivo', 'V1809A': 'vivo', 'V1813A': 'vivo', 'V1732A': 'vivo', 'V1818A': 'vivo',
             'V1809T': 'vivo', 'V1813T': 'vivo',
             'Gionee': 'Gionee',
             'Samsung': 'Samsung', 'S9': 'Samsung',
             'Le X620': 'leshi',
             'M6 Note': 'meizu', 'm3 note': 'meizu', 'M5': 'meizu', 'M1 E ': 'meizu', 'M5 Note': 'meizu',
             'MX6': 'meizu',
             'PRA-AL00': 'honour', 'LND-AL30': 'honour', 'NEM-AL10': 'honour', 'BND-AL10': 'honour',
             'CAM-AL00': 'honour',
             'SCL-TL00': 'honour', 'LLD-AL30': 'honour', 'BLN-AL20': 'honour', 'AUM-AL20': 'honour',
             'JSN-AL00': 'honour',
             'LLD-AL10': 'honour', 'BLN-TL10': 'honour', 'LLD-AL20': 'honour', 'BLN-AL40': 'honour',
             'MYA-AL10': 'honour',
             'LLD-AL00': 'honour', 'JSN-AL00a': 'honour', 'JMM-AL10': 'honour', 'DLI-AL10': 'honour',
             'JMM-AL00': 'honour',
             'LND-AL40': 'honour', 'PLK-AL10': 'honour', 'PLK-TL01H': 'honour', 'KIW-TL00': 'honour'}

user_agent_list = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Dalvik/2.1.0 (Linux; U; Android 10; Redmi K20 Pro Premium Edition MIUI/V11.0.5.0.QFKCNXM)",
    "MicroMessenger Client",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true",

    "Mozilla/5.0 (Linux; Android 7.0; TRT-LX2 Build/HUAWEITRT-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; DUB-AL20 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 10; en-gb; DVC-AN20 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1",
    "Mozilla/5.0 (Linux; Android 10; SCMR-W09 Build/HUAWEISCMR-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Safari/537.36 GDTMobSDK/4.390.1267",
    "Mozilla/5.0 (Linux; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; ANA-AN00 Build/HUAWEIANA-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/12.27 BDOS/1.0 (HarmonyOS 2.2.0) SP-engine/2.37.0 baiduboxapp/12.28.5.10 (Baidu; P1 10) NABar/1.0",
    'Mozilla/5.0 (Linux; Android 10; ANA-AN00 Build/HUAWEIANA-AN00;)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/18.0.1025 Mobile Safari/537.36 hap/1079/huawei com.huawei.fastapp/11.5.1.300 com.xs.yjt/1.0.7 ({\"packageName\":\"InterceptStrategyReceiver\",\"type\":\"url\",\"extra\":\"{}\"})',
    "Mozilla/5.0 (Linux; Android 10; EML-TL00 Build/HUAWEIEML-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 kanqiu/7.5.51.10093/9081 isp/-1 network/-1",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; BKK-AL10 Build/HONORBKK-AL10)",
    "Dalvik/2.1.0 (Linux; U; Android 9; FLA-AL20 Build/HUAWEIFLA-AL20)",
    "Dalvik/2.1.0 (Linux; U; Android 10; ANG-AN00 Build/HUAWEIANG-AN00)",
    "Dalvik/2.1.0 (Linux; U; Android 10; JSN-AL00a Build/HONORJSN-AL00a)",
    "Dalvik/2.1.0 (Linux; U; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00)",
    "Dalvik/2.1.0 (Linux; U; Android 10; JEF-AN00 Build/HUAWEIJEF-AN00)",
    "Dalvik/2.1.0 (Linux; U; Android 10; EML-TL00 Build/HUAWEIEML-TL00)",
    "GDTMobSDK4.400.1272-[Dalvik/2.1.0 (Linux; U; Android 10; OCE-AN10 Build/HUAWEIOCE-AN10)]",
    "Dalvik/2.1.0 (Linux; U; Android 10; OCE-AN10 Build/HUAWEIOCE-AN10)",
    "com.sankuai.meituan/1100150203 (Linux; U; Android 9; zh_CN_#Hans; STF-AL00; Build/HUAWEISTF-AL00; Cronet/90.0.4402.0)",
    "com.ss.android.ugc.aweme/180601 (Linux; U; Android 10; zh_CN_#Hans; VOG-AL00; Build/HUAWEIVOG-AL00; Cronet/TTNetVersion:90dd7cdc 2021-11-10 QuicVersion:68cae75d 2021-08-12)",
    "(Linux;U;Android10;zh - cn;ANG - AN00Build / HUAWEIANG - AN00) AppleWebKit / 533.1(KHTML, likeGecko) MobileSafari / 533.1",
    "com.dragon.read/513 (Linux; U; Android 10; zh_CN_#Hans; ELS-AN00; Build/HUAWEIELS-AN00; Cronet/TTNetVersion:9c4d6484 2021-10-13 QuicVersion:6ad2ee95 2021-04-06)",
    "AiMeiTuan /HUAWEI-10-VOG-AL10-2147-1080-480-11.15.203-1100150203-1bfcad9cc29f44118a13104d40893965a156169413985371406-huawei4"
    "Putong/4.9.8.2 Android/29 HUAWEI/EML-AL00",
    "Mozilla/5.0 (iPad; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 HDQQMusic/10.10.5 Mskin/white Mcolor/22d59cff Bcolor/00000000 skinid[902] NetType/WIFI WebView/UIWebView Released[1] zh-CN DeviceModel/iPad11,3 skin_css/skin2_1_902 Pixel/2224 FreeFlow/0  pixel/1668 model/iPad11,3",
    "Mozilla/5.0 (iPad; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 HDQQMusic/10.10.5 Mskin/white Mcolor/22d59cff Bcolor/00000000 skinid[902] NetType/WIFI WebView/UIWebView Released[1] zh-CN DeviceModel/iPad11,3 skin_css/skin2_1_902 Pixel/2224 FreeFlow/0  pixel/1668 model/iPad11,3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.8(0x18000824) NetType/WIFI Language/zh_CNcom.xs.yjt",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.15 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
    "(iPhone;U;CPUiPhoneOS4_3_2likeMacOSX;en - us) AppleWebKit / 533.17.9(KHTML, likeGecko) Version / 5.0.2Mobile / 8H7Safari / 6533.18.5Quark / 5.4.2.196",

    "Xiaomi-Redmi K30 Ultra__weibo__11.11.2__android__android11_wifi Downloader/2 Cronet",
    "com.ss.android.ugc.aweme/180401 (Linux; U; Android 11; zh_CN; Mi 10 Pro; Build/RKQ1.200826.002; Cronet/TTNetVersion:04953992 2021-07-30 QuicVersion:c9f35932 2021-09-15)",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Mi 10 Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 ImgoTV-aphone/imgotv-aphone-6.8.13.210816",
    "Dalvik/2.1.0 (Linux; U; Android 9; MI 6 MIUI/V11.0.5.0.PCACNXM)",
    "Dalvik/2.1.0 (Linux; U; Android 10; Mi 10 MIUI/V12.0.11.0.QJBCNXM)",
    "Dalvik/2.1.0 (Linux; U; Android 11; Mi 10 Pro Build/RKQ1.200826.002)",
    "Dalvik/2.1.0 (Linux; U; Android 11; M2102K1AC Build/RKQ1.201112.002)",
    "Dalvik/2.1.0 (Linux; U; Android 11; M2102J2SC Build/RKQ1.200826.002)",

    "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; vivo X21 Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3149 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/669 MicroMessenger/8.0.10.1960(0x28000A3D) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Mozilla/5.0 (Linux; Android 6.0; vivo 1610 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.124 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 5.1; vivo X6Plus D Build/LMY47I)",
    "Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001)",

    "Mozilla/5.0 (Linux; Android 11; PCGM00 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/12.27 SP-engine/2.37.0 baiduboxapp/12.28.5.10 (Baidu; P1 11) NABar/1.0",
    "Mozilla/5.0 (Linux; Android 6.0.1; CPH1607 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; PAHM00 Build/QKQ1.191008.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 open_news open_news_u_s/4011",

    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; OE106 Build/OPM1.171019.026)",
    "Dalvik/2.1.0 (Linux; U; Android 11; IN2010 Build/RP1A.201005.001)",
    "Dalvik/2.1.0 (Linux; U; Android 11; KB2000 Build/RP1A.201005.001)",

    "Mozilla/5.0 (Linux; U; Android 5.0; zh-CN; HTC 802t Build/KTU84L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Quark/5.4.2.196 Mobile Safari/537.36",

    "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/BuildID) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",

    "Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Build/NPPS25.137-93-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",

    "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36",
]


def parse_ua():
    ua_string_list = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]

    for i in range(1):
        user_agent = parse(ua_string_list[-1])

        # 操作系统属性
        print(user_agent.os)  #
        print(user_agent.os.family)  #
        print(user_agent.os.version)  #
        print(user_agent.os.version_string)  #

        # 浏览器属性
        print(user_agent.browser)
        print(user_agent.browser.family)
        print(user_agent.browser.version)
        print(user_agent.browser.version_string)

        # 设备属性
        print(user_agent.device)
        print(user_agent.device.family)
        print(user_agent.device.model)
        print(user_agent.device.brand)

        # 判断属性
        print(user_agent.is_pc)
        print(user_agent.is_bot)
        print(user_agent.is_mobile)


def ismobile(ua_string):
    """
    判断是否是手机
    :param ua_string:
    :return:
    """
    return parse(ua_string).is_mobile


def istablet(ua_string):
    """
    判断是否是平板
    :param ua_string:
    :return:
    """
    return parse(ua_string).is_tablet


def ispc(ua_string):
    """
    判断是否是PC
    :param ua_string:
    :return:
    """
    return parse(ua_string).is_pc


def is_touch_capable(ua_string):
    """
    判断是否带触摸功能
    :param ua_string:
    :return:
    """
    return parse(ua_string).is_touch_capable


def is_bot(ua_string):
    """
    判断是否是爬虫
    :param ua_string:
    :return:
    """
    return parse(ua_string).is_bot


def get_ua_browser(ua):
    """

    :param ua:
    :return:
    """
    ret = {
        "browser": "",
        "browser_family": "",
        "browser_version": "",
        "browser_version_string": ""
    }
    try:
        user_agent = parse(ua)
        ret["browser"] = user_agent.browser
        ret["browser_family"] = user_agent.browser.family
        ret["browser_version"] = user_agent.browser.version
        ret["browser_version_string"] = user_agent.browser.version_string
    except:
        pass

    return ret


def get_ua_os(ua):
    """

    :param ua:
    :return:
    """
    ret = {
        "os": "",
        "os_family": "",
        "os_version": "",
        "os_version_string": ""
    }
    try:
        user_agent = parse(ua)
        ret["os"] = user_agent.os
        ret["os_family"] = user_agent.os.family
        ret["os_version"] = user_agent.os.version
        ret["os_version_string"] = user_agent.os.version_string
    except:
        pass

    return ret


def get_ua_device(ua):
    """

    :param ua:
    :return:
    """
    ret = {
        "device": "",
        "device_family": "",
        "device_brand": "",
        "device_model": ""
    }
    try:
        user_agent = parse(ua)
        ret["device"] = user_agent.device
        ret["device_family"] = user_agent.device.family
        ret["device_brand"] = user_agent.device.brand
        ret["device_model"] = user_agent.device.model
    except:
        pass

    return ret


def parse_ua(ua):
    """
    从ua中获取信息
    :param ua:
    :return:
    """
    ua_info = {
        "ua_parse": "",
        "os": "",
        "os_family": "",
        "os_version": "",
        "os_version_string": "",
        "browser": "",
        "browser_family": "",
        "browser_version": "",
        "browser_version_string": "",
        "device": "",
        "device_family": "",
        "device_brand": "",
        "device_model": "",
    }
    try:
        user_agent = parse(ua)
        ua_info["os"] = user_agent.os
        ua_info["os_family"] = user_agent.os.family
        ua_info["os_version"] = user_agent.os.version
        ua_info["os_version_string"] = user_agent.os.version_string
        ua_info["browser"] = user_agent.browser
        ua_info["browser_family"] = user_agent.browser.family
        ua_info["browser_version"] = user_agent.browser.version
        ua_info["browser_version_string"] = user_agent.browser.version_string
        ua_info["device"] = user_agent.device
        ua_info["device_family"] = user_agent.device.family
        ua_info["device_brand"] = user_agent.device.brand
        ua_info["device_model"] = user_agent.device.model
        ua_info["ua_parse"] = user_agent
    except:
        pass

    return ua_info


def get_ua_info(ua_string):
    """
    从ua中获取 os、browser、device
    :param ua_string:
    :return:
    """
    ret = {
        "os": "",
        "browser": "",
        "device": ""
    }

    try:
        ua_string_par = parse(ua_string)
        ret["os"] = ua_string_par.get_os()
        ret["browser"] = ua_string_par.get_browser()
        ret["device"] = ua_string_par.get_device()
    except:
        pass

    return ret


if __name__ == "__main__":
    ua_info = {}
    for i in range(len(user_agent_list)):
        ua_detail_info = parse_ua(user_agent_list[i])
        ua_brief_info = get_ua_info(user_agent_list[i])
        print(ua_detail_info)
        # print(ua_brief_info)
