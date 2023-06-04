import sys

n = int(sys.stdin.readline().strip())
power_list = list(map(int, sys.stdin.readline().strip().split(" ")))
power_max = int(sys.stdin.readline().strip())

ans = i = 0

while i < n:
    ans += power_list[i]
    if power_max - ans in power_list:
        print(power_max)
        break
    elif ans > power_max:
        print(ans - power_list[i])
        break
    else:
        i += 1
