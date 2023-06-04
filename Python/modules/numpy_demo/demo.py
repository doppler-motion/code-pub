import numpy as np

np.zeros(5)

# 创建未初始化的数组，数组类型默认为float
a = np.empty((5, 3))
print(a)

# 修改数据类型
b  = np.zeros((5, 3), dtype=int)
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
