# 网上商城优惠活动
import sys


def get_min_price(price, c_1, c_2, c_3, d=1):
    if d > 2 or c_1 + c_2 + c_3 <= 0:
        return price, 0
    if price < 1:
        return 0, 0

    p = price
    c = 0
    if c_1 > 0:
        # 100-10
        c_num = min(price // 100, c_1)
        p_n = price - 10 * c_num
        p_t, c_t = get_min_price(p_n, 0, c_2, c_3, d + 1)
        if p_t < p:
            p = p_t
            c = c_t + c_num
        elif p_t == p and c_t + c_num < c:
            c = c_t + c_num

    if c_2 > 0:
        c_num = 1
        p_n = price * 0.92
        p_t, c_t = get_min_price(p_n, c_1, 0, c_3, d + 1)
        if p_t < p:
            p = p_t
            c = c_t + c_num
        elif p_t == p and c_t + c_num < c:
            c = c_t + c_num

    if c_3 > 0:
        c_num = min((price // 5) + 1, c_3)
        p_n = max(price - 5 * c_num, 0)
        p_t, c_t = get_min_price(p_n, c_1, c_2, 0, d + 1)
        if p_t < p:
            p = p_t
            c = c_t + c_num
        elif p_t == p and c_t + c_num < c:
            c = c_t + c_num
    return p, c


if __name__ == "__main__":
    # 读取第一行的n
    coupon_list = sys.stdin.readline().strip().split()
    c_1 = int(coupon_list[0])
    c_2 = int(coupon_list[1])
    c_3 = int(coupon_list[2])
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        price = int(sys.stdin.readline().strip())
        # 把每一行的数字分隔后转化成int列表
        p_n, c_n = get_min_price(price, c_1, c_2, c_3)
        print(int(p_n), int(c_n))
