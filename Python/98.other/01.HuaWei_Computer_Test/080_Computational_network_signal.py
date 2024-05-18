# 计算网络信号
from collections import deque

n, m = map(int, input().split())
arr = [int(_) for _ in input().split()]
mp = [[0 for _ in range(m)] for _ in range(n)]
ans = [[0 for _ in range(m)] for _ in range(n)]
now = 0
x, y = 0, 0
for i in range(n):
    for j in range(m):
        mp[i][j] = arr[now]
        if arr[now] > 0:
            x, y = i, j
        now += 1
a, b = map(int, input().split())
q = deque()
q.append((x, y))
ans[x][y] = mp[x][y]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while len(q) > 0:
    (nowx, nowy) = q.popleft()
    for i in range(4):
        nx = dx[i] + nowx
        ny = dy[i] + nowy
        if nx >= 0 and nx < n and ny < m and ny >= 0 and mp[nx][ny] != -1 and ans[nowx][nowy] >= 1 and ans[nx][ny] == 0:
            ans[nx][ny] = ans[nowx][nowy] - 1
            q.append((nx, ny))
print(ans[a][b])
