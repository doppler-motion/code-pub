# 单核CPU任务调度

import functools
import sys


def comp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        return 0
    else:
        return 1


def find(tasks, time):
    for task in tasks:
        if task[3] == time:
            return task
    return None


# 处理输入
# 不确定多少行输入
tasks = []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    tasks.append([int(x) for x in line.split(" ")])

# print (tasks)

time = 0
waiting = []
while len(tasks) > 0:
    cur = find(tasks, time)

    if cur is not None:
        waiting.append(cur)
        # 按照优先级排序
        waiting = sorted(waiting, key=functools.cmp_to_key(comp))
        # print (tasks)
        cur = waiting[0]
    else:
        if len(waiting) != 0:
            cur = waiting[0]

    if cur is not None:
        cur[2] -= 1
        if cur[2] == 0:
            print(str(cur[0]) + " " + str(time + 1))
            tasks.remove(cur)
            waiting.remove(cur)

    time += 1
