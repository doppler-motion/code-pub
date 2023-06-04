# 寻找充电设备组合
import sys

n = sys.stdin.readline().strip()
n = int(n)

line = sys.stdin.readline().strip()
p = list(map(int, line.split()))

limit = sys.stdin.readline().strip()
limit = int(limit)

dp = [[0] * (limit + 2) for _ in range(n + 1)]
p.sort()
for i in range(1, n + 1):
    for j in range(0, limit + 2):
        if j < p[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - p[i - 1]] + p[i - 1], dp[i - 1][j])
# print(len(dp), len(dp[0]))
ans = max(dp[n])
print(ans)
