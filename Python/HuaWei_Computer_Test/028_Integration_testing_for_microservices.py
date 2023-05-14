# 微服务的集成测试

import sys

line0 = sys.stdin.readline().strip()
n = int(line0)
map = []
for i in range(n):
    map.append([0] * n)
for i in range(n):
    line = sys.stdin.readline().strip().split()
    for j in range(n):
        map[i][j] = int(line[j])

kk = int(input())
time = 0
cost = []
for i in range(n):
    cost.append(map[i][i])


def test_end(cost):
    for i in range(n):
        if cost[i]:
            return 0
    return 1


while (not test_end(cost)):
    runnable = []
    for i in range(n):
        flag = 1
        for j in range(n):
            if i == j:
                continue
            if map[i][j] != 0:
                flag = 0
                break
        if flag:
            runnable.append(i)

    runtime = 99999999
    for k in runnable:
        if cost[k] and cost[k] < runtime:
            runtime = cost[k]

    time += runtime
    for k in runnable:
        if cost[k] > 0:
            cost[k] -= runtime
        else:
            cost[k] = 0
        if cost[k] == 0:
            for i in range(n):
                map[i][k] = 0
    if (cost[kk - 1] == 0):
        break
#    print(map, runnable,cost)
print(time)
