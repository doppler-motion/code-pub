# 日志采集系统

lis = list(map(int, input().split()))
dp = [0] * len(lis)
for i in range(len(lis)):
    delta = 0
    for j in range(i):
        delta += lis[j] * (i - j)
    if sum(lis[:i + 1]) > 100:
        dp[i] = 100 - delta
    else:
        dp[i] = sum(lis[:i + 1]) - delta
print(max(dp))
