import time
import datetime

from loguru import logger

logger.info(time.localtime().tm_min)

logger.info(time.localtime(1644741268).tm_min)

# 当前时间
nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logger.info("now 4.time: ", nowTime)

#  时间戳、格式化时间 *********************************
timeStamp = time.time()  # 1644741268.9751265
timeArray = time.localtime(timeStamp)  # 将时间戳格式化, 4.time.struct_time(tm_year=2022, tm_mon=2, tm_mday=13, tm_hour=16, tm_min=35, tm_sec=14, tm_wday=6, tm_yday=44, tm_isdst=0)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)  # 2022-02-13 16:37:20
otherStyleTime1 = time.strftime("%d-%m-%Y %H:%M:%S", timeArray)  # 13-02-2022 16:37:20

timeStamp = time.time()  # 1644741268.9751265
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)  # 4.time.struct_time(tm_year=2022, tm_mon=2, tm_mday=13, tm_hour=16, tm_min=35, tm_sec=14, tm_wday=6, tm_yday=44, tm_isdst=0)
dateStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")  # 2022-02-13 16:37:20

# 字符串时间 转换为 时间戳 *****************************

# 字符串类型的时间1

time_str1 = "2022-02-13 16:37:20"

# 转换为时间数组

timeArray = time.strptime(time_str1, "%Y-%m-%d %H:%M:%S")  # 4.time.struct_time(tm_year=2022, tm_mon=4, tm_mday=20, tm_hour=18, tm_min=20, tm_sec=53, tm_wday=2, tm_yday=110, tm_isdst=-1)

# 字符串类型的时间2

time_str2 = "Sun Feb 12 16:37:20 +0000 2022"

timeArray1 = time.strptime(time_str2, "%a %b %d %H:%M:%S %z %Y")

# 转为时间戳

timeStamp = time.mktime(timeArray1)

time_str3 = "2022-02-13 16:37:20"

otherStyleTime2 = datetime.datetime.strptime(time_str3, "%Y-%m-%d %H:%M:%S").strftime("%Y/%m/%d %H:%M:%S")  # 2022/02/13 16:37:20

# 日期的加减**********************************

d1 = datetime.datetime.strptime("2021-02-12 17:23:23", "%Y-%m-%d %H:%M:%S")
d2 = datetime.datetime.strptime("2021-02-09 17:23:23", "%Y-%m-%d %H:%M:%S")

time_delta = d1 - d2  # 3 days, 0:00:00, 类型：datetime.timedelta

n_days = time_delta.days  # 3

now = datetime.datetime.now()  # 2022

now_time = now.strftime('%Y-%m-%d %H:%M:%S')
before_two_hour = (now - datetime.timedelta(days=10)).strftime('%Y-%m-%d %H:%M:%S')

logger.info(now_time, before_two_hour)