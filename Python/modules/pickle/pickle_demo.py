import pickle

"""
更好的选择是： ZOOB
"""

tup = ("I love python", {1, 2, 3}, None)

# 使用dumps()函数将tup1转成p1
p1 = pickle.dumps(tup)
print("p1: ", p1)

# 使用loads()函数将二进制对象转换成python对象
t1 = pickle.loads(p1)
print("t1: ", t1)

# 使用dump()函数将python对象转换成二进制文件
with open("a.pkl", "wb") as f:
    pickle.dump(tup, f)

# 使用load()函数将二进制文件转换成python对象
with open("a.pkl", "rb") as f:
    t2 = pickle.load(f)
print("t2: ", t2)
