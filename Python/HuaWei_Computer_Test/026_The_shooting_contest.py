# 投篮大赛

ops = input().split()
l = len(ops)
result = []
j = -1
flag = 1
for i in range(l):
    if ops[i].isdigit() or '-' in ops[i]:
        result.append(int(ops[i]))
        j += 1
    elif ops[i] == '+' and len(result) >= 2:
        result.append(result[j] + result[j - 1])
        j += 1
    elif ops[i] == 'D' and len(result) >= 1:
        result.append(result[j] * 2)
        j += 1
    elif ops[i] == 'C' and len(result) >= 1:
        result.pop()
        j -= 1
    else:
        flag = 0
if flag:
    num = sum(result)
    print(num)
else:
    print('-1')
