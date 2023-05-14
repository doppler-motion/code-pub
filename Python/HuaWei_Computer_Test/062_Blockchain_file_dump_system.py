# 区块链文件转存技术

tol = int(input())

li = list(map(int, input().split()))
le = len(li)
ma = tol
i = 0
j = 0
tol1 = tol
while j < le:
    if tol - li[j] >= 0:
        tol -= li[j]
        if tol == 0:
            ma = 0
            break
        j += 1
    elif tol - li[j] < 0:
        tol -= li[j]
        while tol < 0:
            tol += li[i]
            i += 1
        if tol == 0:
            ma = 0
            break
        j += 1
    if tol < ma:
        ma = tol

print(tol1 - ma)

