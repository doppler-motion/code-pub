# 贪心的商人

number, days = map(int, input().split())
item = list(map(int, input().split()))
item_price = [list(map(int, input().split())) for _ in range(number)]

res = 0
for i in range(number):
    for j in range(days - 1):
        purchase = item_price[i][j]
        selling = item_price[i][j + 1]
        if selling > purchase:
            res += (selling - purchase) * item[i]

print(res)
