# 开心消消乐

def func(m, n):
    M[m][n] = 0
    for i in [min(m + 1, len(M) - 1), m, max(m - 1, 0)]:
        for j in [min(n + 1, len(M[0]) - 1), n, max(n - 1, 0)]:
            if M[i][j] == 1:
                func(i, j)


[a, b] = list(map(int, input().split()))
M = []
for i in range(a):
    M.append(list(map(int, input().split())))
step = 0
while True:
    One = False
    for i in range(a):
        for j in range(b):
            if M[i][j] == 1:
                One = True
                step += 1
                func(i, j)
    if One == False:
        break

print(step)
