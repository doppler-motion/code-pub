# 货币单位换算
T = int(input())
Y = ['CNY', 'HKD', 'JPY', 'EUR', 'GBP']
F = ['fen', 'cents', 'sen', 'eurocents', 'pence']
cost = [100, 123, 1825, 14, 12]
result = 0
for k in range(T):
    st = input()
    left = 0
    for i in range(5):
        if Y[i] in st:
            num = ''
            j = 0
            while st[j] >= '0' and st[j] <= '9':
                num = num + st[j]
                j = j + 1
            num = int(num)
            result = result + num * 100 / cost[i] * cost[0]
            while j < len(st) and not (st[j] >= '0' and st[j] <= '9'):
                j = j + 1
            left = j
    for i in range(4, -1, -1):
        if F[i] in st:
            num = ''
            j = left
            while st[j] >= '0' and st[j] <= '9':
                num = num + st[j]
                j = j + 1
            num = int(num)
            result = result + num / cost[i] * cost[0]
            break
print(int(result))
