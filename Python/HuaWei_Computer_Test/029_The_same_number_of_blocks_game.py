# 相同数字的积木游戏

n = int(input())
ls = []
dict_ = {}
distance = -1
for i in range(n):
    ls.append(int(input()))
for i in range(n):
    if ls[i] not in dict_:
        dict_[ls[i]] = i
    else:
        distance = i - dict_[ls[i]]
print(distance)
