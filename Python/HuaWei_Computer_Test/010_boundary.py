# 分界线
import sys


def divine():
    # 读取第一行的n
    b = []
    for i in range(2):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        c = []
        d = []
        a = list(map(str, line.split()))
        for j in range(len(a)):
            for k in a[j]:
                c.append(k)
            c.sort()
            d.append(c)
            c = []
        b.append(d)
    for i in range(len(b[1])):
        if b[1][i] in b[0]:
            b[0].remove(b[1][i])
        else:
            return ('false')
    return ('true')


print(divine())
