# 计算数组中心位置

# 计算num_list的乘积
def calc_pd(num_list):
    pd = 1
    for num in num_list:
        pd *= num

    return pd


def solution_01():
    # 处理输入
    num_list = input().split(" ")
    num_list = [int(num) for num in num_list]

    ans = -1
    for i in range(0, len(num_list)):
        if i == 0:
            l_pd = 1
            r_pd = calc_pd(num_list[1:])
        elif i == len(num_list) - 1:
            l_pd = calc_pd(num_list[0: -1])
            r_pd = 1
        else:
            l_pd = calc_pd(num_list[0: i])
            r_pd = calc_pd(num_list[i + 1:])

        if l_pd == r_pd and ans == -1:
            ans = i

    return ans


if __name__ == '__main__':
    ans = solution_01()
    print(ans)
