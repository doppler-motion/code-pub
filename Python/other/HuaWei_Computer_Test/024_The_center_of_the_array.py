# 数组中心位置

a = input().split()
b = [int(i) for i in a]
l = 1
r = 1
mid = []
for i in range(0, len(b)):
    for j in b[:i]:
        l = j * l
    for k in b[i + 1:]:
        r = r * k
    if l == r:
        mid.append(i)
    l = 1
    r = 1
if len(mid) > 0:
    print(mid[0])
else:
    print("-1")
