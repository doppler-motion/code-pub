import sys

m = int(sys.stdin.readline().strip())
file_size_list = list(map(int, sys.stdin.readline().strip().split(" ")))
n, ans = len(file_size_list), 0
i = 0

while i < n:
    max_size = file_size_list[i]
    for j in range(i + 1, n):
        if max_size < m:
            max_size += file_size_list[j]
            if max_size < m:
                ans = max(max_size, ans)
        else:
            break
print(ans)
