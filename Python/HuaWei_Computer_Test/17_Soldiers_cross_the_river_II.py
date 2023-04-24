#  士兵过河


n = int(input())
t = int(input())
a = list(map(int, input().split()))

a.sort()

num_alive = 0
min_time = float('inf')

for i in range(n):
    time = a[i]
    if time <= t:
        num_alive += 1
        min_time = min(min_time, time)

i, j = 0, n - 1
while i <= j:
    if a[i] + a[j] <= t:
        num_alive += 2
        min_time = min(min_time, max(a[i], a[j]))
        i += 1
        j -= 1
    else:
        j -= 1

for i in range(n - 2):
    time = a[i] + a[i + 1] * 10
    if time <= t:
        num_alive += 2
        min_time = min(min_time, max(a[i], a[i + 1]))

print(num_alive, min_time)
