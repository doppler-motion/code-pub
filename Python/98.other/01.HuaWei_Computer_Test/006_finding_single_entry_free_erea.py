# 查找单入口空闲区域
import sys

row_all, col_all = input().strip().split(" ")
row_all = int(row_all)
col_all = int(col_all)

data = []
for i in range(row_all):
    col = input().strip().split(" ")
    data.append(col)

node_list = list()
start_row = [0, row_all - 1]
start_col = [0, col_all - 1]
for row in start_row:
    for col in range(col_all):
        if data[row][col] == "O":
            if (row, col) not in node_list:
                node_list.append((row, col))
for row in range(row_all):
    for col in start_col:
        if data[row][col] == "O":
            if (row, col) not in node_list:
                node_list.append((row, col))

if len(node_list) == 0:
    print("NULL")

max_size = 0
max_row, max_col = 0, 0
flag = False
for row1, col1 in node_list:
    temp_node_list = []
    temp_size = 1
    temp_node_list.append((row1, col1))
    overed_path = []
    while temp_node_list:
        row, col = temp_node_list.pop(0)
        overed_path.append((row, col))
        # 上下左右四个方向搜索
        # 上
        if 0 <= row - 1:
            if row - 1 == 0 and data[row - 1][col] == "O" and (row - 1, col) != (row1, col1):
                temp_size = 0
                break
            if data[row - 1][col] == "O":
                if (row - 1, col) not in overed_path and (row - 1, col) not in temp_node_list:
                    temp_size += 1
                    temp_node_list.append((row - 1, col))

        if row + 1 <= row_all - 1:
            if row + 1 == row_all - 1 and data[row + 1][col] == "O" and (row + 1, col) != (row1, col1):
                temp_size = 0

                break
            if data[row + 1][col] == "O":
                if (row + 1, col) not in overed_path and (row + 1, col) not in temp_node_list:
                    temp_size += 1
                    temp_node_list.append((row + 1, col))
        # 左
        if 0 <= col - 1:
            if col - 1 == 0 and data[row][col - 1] == "O" and (row, col - 1) != (row1, col1):
                temp_size = 0

                break
            if data[row][col - 1] == "O":
                if (row, col - 1) not in overed_path and (row, col - 1) not in temp_node_list:
                    temp_size += 1
                    temp_node_list.append((row, col - 1))
        # 右
        if col + 1 <= col_all - 1:
            if col + 1 == col_all - 1 and data[row][col + 1] == "O" and (row, col + 1) != (row1, col1):
                temp_size = 0

                break
            if data[row][col + 1] == "O":
                if (row, col + 1) not in overed_path and (row, col + 1) not in temp_node_list:
                    temp_size += 1
                    temp_node_list.append((row, col + 1))
    if temp_size > max_size:
        max_size = temp_size
        max_row = row1
        max_col = col1
    if temp_size == max_size and temp_size > 0:
        flag = True
if max_size == 0:
    print("NULL")
else:
    print(" ".join([str(max_row), str(max_col), str(max_size)]))
