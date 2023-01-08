import pandas as pd

# 创建DataFrame
d = {'one': {'a': 1, 'b': 2, 'c': 3}, 'two': {'a': 4, 'b': 5, 'c': 6}, 'three': {'a': 7, 'b': 8, 'c': 9}}
df = pd.DataFrame(d)
print(df)
# 保存为csv文件
df.to_csv("test_files/test1.csv")
# 从csv文件读取信息
df1 = pd.read_csv("test_files/test1.csv")
print(df1)
# 获取列名
print(df1.columns)
print(type(df1.columns))
print(list(df1.columns.values))

# 转为dict
print(df1.to_dict())
print(pd.DataFrame(df1.to_dict()))

# 指定列之间的求和
df.eval("new_col = {add_column}".format(add_column="+".join(df.columns.values.tolist()[1:])), inplace=True)
print(df)

# 添加新的行
df.iloc["row"] = df.apply(lambda x: x.sum(), axis=0)
df.loc["row"] = [1, 2, 3, 4]

# 修改列名
# df.rename(columns={oldname1:newname1,oldname2:newname2},inplace=True)

# print(df)
# data = pd.read_csv("test_files/test.csv")
# columns_names = data.columns
# print(columns_names)
# print(type(columns_names))
# print(columns_names[0])
# for columns_name in columns_names:
#     print(columns_name)
