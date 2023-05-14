# 最多几个直角三角形
import sys

N = int(input())
while N > 0:
    vec = input().split()
    n = int(vec[0])
    arr = []
    for i in range(1, len(vec)):
        arr.append(int(vec[i]))
    arr.sort()
    s = []
    N -= 1
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                a = arr[i]
                b = arr[j]
                c = arr[k]
                if a + b > c and a * a + b * b == c * c:
                    if [a, b, c] not in s:
                        s.append([a, b, c])
    print(len(s))
