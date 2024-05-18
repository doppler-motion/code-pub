# 关联端口组合并

import sys

m = int(input())
if m < 1 or m > 10:
    print([[]])
else:
    ports = []
    res = []
    for _ in range(m):
        line = sys.stdin.readline().strip()
        group = set(map(int, line.split(',')))
        ports.append(group)
    res = []
    visited = [0] * m
    for i in range(len(ports)):
        if visited[i] == 1: continue
        if len(ports[i]) < 2:
            res.append(list(ports[i]))
            continue
        temp = ports[i]
        for j in range(i + 1, len(ports)):
            if len(temp & ports[j]) >= 2:
                temp |= ports[j]
                visited[j] = 1
        flag = 0
        for k in range(len(res)):
            x = res[k]
            if len(temp & set(x)) >= 2:
                temp |= set(x)
                list_temp = list(temp)
                list_temp.sort()
                res[k] = list_temp
                flag = 1
        if not flag:
            list_temp = list(temp)
            list_temp.sort()
            res.append(list_temp)
    res_s = '['
    for x in res:
        res_s += '['
        for y in x:
            res_s += str(y) + ','
        res_s = res_s[:-1]
        res_s += '],'
    res_s = res_s[:-1] + ']'
    print(res_s)
