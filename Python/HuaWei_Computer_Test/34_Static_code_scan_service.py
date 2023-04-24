# 静态代码扫描

scan = int(input())
doc = input().split(" ")
cache = input().split(" ")
cache = [int(i) for i in cache]
dic = {}
dicScan = {}
for i in range(len(doc)):
    if dic.get(int(doc[i])):
        dic[int(doc[i])] += 1
    else:
        dic[int(doc[i])] = 1
        dicScan[int(doc[i])] = cache[i]

cos = 0
for d, times in dic.items():
    cos += min(dicScan[d] + scan, times * dicScan[d])

print(cos)
