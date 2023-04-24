# 任务执行总时长
import sys

line = sys.stdin.readline().strip()
ta, tb, num = map(int, line.split(","))

if num == 0:
    ans = []
elif ta == tb:
    ans = [num * ta]
else:
    if ta > tb:
        ta, tb = tb, ta
    ans = [ta * num]
    minus = tb - ta
    for i in range(num):
        ans.append(ans[-1] + minus)

print(ans)
