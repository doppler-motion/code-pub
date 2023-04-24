# https://blog.csdn.net/2301_76848549/article/details/130163180  快递投放问题

info = list(map(int, input().split(' ')))
dict = {}
dict1 = {}
for i in range(info[0]):
    package = input().split(' ')
    dict[package[0]] = package[1: 3]

for i in range(info[1]):
    ban = input().split(' ')
    for j in ban[2:]:
        if j in dict1:
            dict1[j].append(ban[0:2])
        else:
            dict1[j] = [ban[0:2]]
out = []
for key in dict:
    if key in dict1:
        for i in range(len(dict1[key])):
            if sorted(dict1[key][i]) == sorted(dict[key]):
                out.append(key)

if out:
    out = sorted(out)
    print(' '.join(out))
else:
    print('none')
