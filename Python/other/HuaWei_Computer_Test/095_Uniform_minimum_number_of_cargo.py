#  https://blog.csdn.net/A_D_I_D_A_S/article/details/129323811
# 统一限载货物数最小值
def opt(goods, k):
    n = len(goods)
    sum = [0] * (n + 1)
    dp = [[0 for i in range(n + 1)] for j in range(2)]
    for i in range(0, n):
        sum[i + 1] = goods[i] + sum[i]
        dp[0][i + 1] = float('inf')
        dp[1][i + 1] = float('inf')
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for c in range(i - 1, j):
                dp[i % 2][j] = min(dp[i % 2][j], max(dp[(i - 1) % 2][c], sum[j] - sum[c]))

    return dp[k % 2][n]


def minimum_capacity():
    length = int(input())
    goods = input().split(" ")
    goods = [int(good) for good in goods]
    types = input().split(" ")
    k = int(input())

    dry_goods = []
    wet_goods = []
    for idx, type in enumerate(types):
        if type == "0":
            dry_goods.append(goods[idx])
        else:
            wet_goods.append(goods[idx])

    dry_ans = opt(dry_goods, k)
    wet_ans = opt(wet_goods, k)

    ans = max(dry_ans, wet_ans)
    print(ans)


if __name__ == '__main__':
    minimum_capacity()
