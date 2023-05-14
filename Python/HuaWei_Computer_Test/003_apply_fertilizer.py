# 不爱施肥的小布

import math
import sys


def cal(k, fields):
    days = 0
    for i in range(len(fields)):
        days += math.ceil(fields[i] / float(k))
    return days


def do_job():
    params = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    fields = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    m = params[0]
    n = params[1]

    if n < len(fields):  # 如果施肥的天数 < 田地数
        print(-1)
    elif n == len(fields):  # 如果施肥的天数 == 田地数
        print(max(fields))
    else:  # 如果施肥的天数 > 田地数
        fields = sorted(fields)
        left = 0
        right = fields[len(fields) - 1]

        result = -1
        while left + 1 < right:
            k = int(math.ceil(float(left + right) / 2))

            res = cal(k, fields)

            if res - n > 0:
                left = k
            else:
                result = k
                right = k
        print(result)


if __name__ == "__main__":
    do_job()
