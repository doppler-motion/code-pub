# 求字典的最大Value值对应的Key值
dic = {"a": 1, "b": 2, "c": 3, "d": 4}
ans = max(dic, key=lambda x: dic[x])
# ans = max(dic, key=dic.get)  # 利用get方法
print(ans)

# 若字典的最大Value值有多个， 返回的的Key值(返回第一个)
dic = {"a": 1, "c": 4, "r": 9, "l": 4, "d": 9}
ans = max(dic, key=lambda x: dic[x])
print(ans)

# 按照key或者value对字典进行排序
# 按照key进行排序
sdic = sorted(dic.items(), key=lambda it: it[0], reverse=True)
print(sdic)
# 按照value进行排序
sdic = sorted(dic.items(), key=lambda it: it[1], reverse=False)
