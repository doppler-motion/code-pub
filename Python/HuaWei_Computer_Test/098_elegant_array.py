# 优雅数组
length, k = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
isK = False
hash_m = {}
for win_len in range(1, length + 1):
    i = 0
    j = i + win_len
    while j <= length:
        if j - i < k:
            j += 1
            i += 1
            continue
        else:
            for e in nums[i:j]:
                hash_count = hash_m.get(e, 0)
                if hash_count == k - 1:
                    isK = True

                hash_m[e] = hash_count + 1
            hash_m.clear()
        j += 1
        i += 1
        if isK:
            count += 1
            isK = False
print(count)
