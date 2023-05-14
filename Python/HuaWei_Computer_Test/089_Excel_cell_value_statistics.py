#  Execl 单元格数值统计


import re

params = input().split()
rows = int(params[0])
cols = int(params[1])

matrix = [[0] * cols for _ in range(rows)]
for i in range(rows):
    matrix[i] = input().split()

for i in range(rows):
    for j in range(cols):
        if matrix[i][j][0] == '=':
            if '+' in matrix[i][j]:
                op = matrix[i][j].split('+')
                op1 = op[0]
                op2 = op[1]

                if re.match(r'^-?\d+(\.\d+)?$', op1[1:]):
                    num1 = int(op1[1:])
                else:

                    num1 = int(matrix[int(op1[2:]) - 1][ord(op1[1]) - 65])

                if re.match(r'^-?\d+(\.\d+)?$', op2):
                    num2 = int(op2)
                else:
                    num2 = int(matrix[int(op2[1:]) - 1][ord(op2[0]) - 65])

                matrix[i][j] = str(num1 + num2)
            elif '-' in matrix[i][j]:
                op = matrix[i][j].split('-')
                op1 = op[0]
                op2 = op[1]

                if re.match(r'^-?\d+(\.\d+)?$', op1[1:]):
                    num1 = int(op1[1:])
                else:
                    num1 = int(matrix[int(op1[2:]) - 1][ord(op1[1]) - 65])

                if re.match(r'^-?\d+(\.\d+)?$', op2):
                    num2 = int(op2)
                else:
                    num2 = int(matrix[int(op2[1:]) - 1][ord(op2[0]) - 65])

                matrix[i][j] = str(num1 - num2)
            else:
                matrix[i][j] = str(int(matrix[int(matrix[i][j][2:]) - 1][ord(matrix[i][j][1]) - 65]))

if __name__ == '__main__':

    output = input().split(':')

    res = 0
    for i in range(int(output[0][1:]) - 1, int(output[1][1:])):
        for j in range(ord(output[0][0]) - 65, ord(output[1][0]) - 64):
            res += int(matrix[i][j])

    print(res)
