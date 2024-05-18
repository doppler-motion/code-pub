# 光伏场地建设

import functools
import copy


def maxTime(mat, threshold, c):
    m, n = len(mat), len(mat[0])
    E = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            E[i][j] = E[i - 1][j] + E[i][j - 1] - E[i - 1][j - 1] + mat[i - 1][j - 1]
    ans = 0

    for i in range(c, m + 1):
        for j in range(c, n + 1):
            if (E[i][j] - E[i - c][j] - E[i][j - c] + E[i - c][j - c] >= threshold):
                ans = ans + 1
    return ans


size_nums = [int(x) for x in input().split(" ")]
n = size_nums[0]
m = size_nums[1]
c = size_nums[2]
k = size_nums[3]
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(" ")])
print(maxTime(matrix, k, c))
