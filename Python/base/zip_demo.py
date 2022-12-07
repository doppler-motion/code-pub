a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
d = ["a", "b", "c"]

zipped = zip(a, b)  # 返回一个对象
print("zipped: ", zipped)
list1 = list(zipped)  # 返回一个列表
print(f"list1: {list1}")
dict1 = dict(zip(d, a))  # 返回一个字典
print(f"dict1: {dict1}")
list2 = list(zip(a, c))  # 元素与较短的列表保持一致
print(f"list2: {list2}")
a1, a2 = zip(*zip(a, b))  # *zip可理解为解压，返回二维矩阵式
print("a1: ", a1)
print("a2: ", a2)
