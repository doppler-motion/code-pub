# 通信误码

import sys

n = int(input())
line = None
# for lines in sys.stdin:
line = sys.stdin.readline().strip().split()
# line = input().split()
# if line is not None:
id_to_freq = dict()
max_freq = 0
max_freq_id = []
nums = []
for i in line:
    nums.append(i)
    if i == "0": continue
    if i not in id_to_freq:
        id_to_freq[i] = 1
    else:
        id_to_freq[i] += 1

    if id_to_freq[i] > max_freq:
        max_freq = id_to_freq[i]
        max_freq_id = [i]
    elif id_to_freq[i] == max_freq:
        max_freq_id.append(i)
# print(id_to_freq, max_freq, max_freq_id)

if n == 0:
    print(0)
else:
    min_len = float("inf")
    for id in max_freq_id:
        start = -1
        end = -1
        freq = 0
        for i in range(len(nums)):
            if nums[i] == id:
                freq += 1
                if start == -1:
                    start = i
                if freq == id_to_freq[nums[i]]:
                    end = i
        min_len = min(min_len, end - start + 1)
    print(min_len)
