n = int(input())
file = {x: [] for x in range(6)}
p = {x: [] for x in range(6)}
out = []
s = 0
for i in range(n):
    a = list(input().split())
    if a[0] == 'IN':
        s += 1
        file[int(a[1])].append(int(a[2]))
        p[int(a[1])].append(s)
    else:
        j = int(a[1])
        if file[j]:
            ans = max(file[j])
            b = 0
            for k in range(len(file[j])):
                if file[j][k] == ans:
                    b = k
                    break
            print(p[j][b])
            file[j].remove(file[j][b])
            p[j].remove(p[j][b])
        else:
            print('NULL')
