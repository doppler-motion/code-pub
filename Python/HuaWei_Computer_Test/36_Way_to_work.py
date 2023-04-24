# 上班之路
import sys

t, c = map(int, input().split())
n, m = map(int, input().split())

matrix = [input().strip() for i in range(n)]


def solve_method():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "S":
                path = set()
                path.add(i * m + j)
                return "YES" if dfs(i, j, 0, 0, 0, path) else "NO"
    return "NO"


offsets = [[-1, 0, 1], [1, 0, 2], [0, -1, 3], [0, 1, 4]]


def dfs(si, sj, ut, uc, lastDirect, path):
    if matrix[si][sj] == "T":
        return True

    for offset in offsets:
        direct = offset[2]
        newI, newJ = si + offset[0], sj + offset[1]

        flag1, flag2 = False, False

        if 0 <= newI < n and 0 <= newJ < m:
            pos = newI * m + newJ
            if pos in path:
                continue

            if lastDirect != 0 and lastDirect != direct:
                if ut + 1 > t:
                    continue
                flag1 = True

            if matrix[newI][newJ] == "*":
                if uc + 1 > c:
                    continue
                flag2 = True

            path.add(pos)

            res = dfs(newI, newJ, ut + flag1, uc + flag2, direct, path)

            if res:
                return True

            path.remove(pos)
    return False


print(solve_method())
