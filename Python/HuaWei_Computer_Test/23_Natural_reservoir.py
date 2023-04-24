# 天然蓄水库

import sys
from collections import deque

line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

res = 0
res_t = (0, 0)
s = deque()

for i in range(len(values)):
    r_h = values[i]
    if not s:
        s.append(i)
        continue

    l = s[-1]
    if values[l] >= r_h:
        s.append(i)

    while values[l] < r_h:
        s.pop()
        if s:
            l = s[-1]
        else:
            break

    if values[l] != r_h:
        s.append(i)

    l_h = values[l]
    w_h = min(l_h, r_h)
    tmp = 0
    for j in range(l + 1, i):
        tmp += w_h - (values[j] if values[j] < w_h else w_h)

    if tmp > res:
        res = tmp
        res_t = (l, i)

if res == 0:
    print(0)
else:
    print("{} {}:{}".format(res_t[0], res_t[1], res))
