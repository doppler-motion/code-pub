import numpy as np

np.zeros(5)

# 创建未初始化的数组，数组类型默认为float
a = np.empty((5, 3))
print(a)

# 修改数据类型
b = np.zeros((5, 3), dtype=int)
print(b)

# 从已有数组转换为ndarray
# 列表
l1 = [1, 2, 3]
l_arr1 = np.asarray(l1)
print(type(l_arr1))

# 数值范围创建数组
c = np.arange(0, 10, 1)
print(c)
print(type(c))

# 生成一个一维数组，等差数列
line_array = np.linspace(0, 10, 20)
print(line_array)

# 生成等比数列
log_array = np.logspace(1, 2, num=10, base=3)
print(log_array)

# 切片操作
d_array = np.arange(0, 10, 1)
print(d_array)
print(d_array[0:1])

# 生成 均等分布的数值
x = np.linspace(0, 1, 10)
print(x)

# 生成服从均值为0，标准差为1的正态分布随机数
num1 = np.random.randn(10, 2)
# print(num1)

# 向量内积
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.dot(a, b)

# 矩阵内积
A = np.arange(10).reshape(5, 2)
B = np.arange(8).reshape(2, 4)
C = np.dot(A, B)

print(f"vector dot: {c}\n, matrix dot: {C}")

# 简易版的全连接层
x = np.random.randn(10, 2)  # 输入
w = np.random.randn(2, 10)  # 权重
b = np.random.randn(10)  # 偏置

y = np.dot(x, w) + b
print(y)

# 数组取值
arr1 = np.arange(10).reshape(5, 2)
print(f"arr1: {arr1}")
arr_t = np.array([0, 1])
get_val = arr1[np.arange(2), arr_t]
print("get_val: ", get_val)

# 采样
p = [0.01, 0.25, 0.09, 0.35, 0.13, 0.17]
choice_num = np.random.choice(list(range(6)), p=p, replace=False)  # 按概率无返回的随机选取1个元素
print("choice_num: ", choice_num)
