# 工作安排

T, n = map(int, input().split())
Time_pay = []
while True:
    try:
        time, num = map(int, input().split())
        Time_pay.append((time, num))
    except:
        break
time = [i[0] for i in Time_pay]
value = [i[1] for i in Time_pay]
total_time = T
dp = [0] * (total_time + 1)
for i in range(len(time)):
    for j in range(total_time, time[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - time[i]] + value[i])
print(dp[-1])
