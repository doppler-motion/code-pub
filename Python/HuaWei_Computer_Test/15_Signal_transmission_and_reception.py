# https://blog.csdn.net/qfc_128220/article/details/128714601

# 输入获取
m, n = map(int, input().split())
arr = list(map(int, input().split()))


def common(stack, anth, ret, i, j):
    # 如果栈顶天线比anth[i][j]，则anth[i][j]必然能接收到栈顶天线的信号，并且还能继续接收栈顶前面一个天线的信号（递减栈，栈顶前面天线高度必然大于栈顶天线高度）
    while len(stack) > 0 and anth[i][j] > stack[-1]:
        ret[i][j] += 1
        stack.pop()
    # 走到此步，如果stack还有值，那么由于是递减栈，因此此时栈顶天线高度必然
    if len(stack) > 0:
        # 如果栈顶天线高度 == anth[i][j]，那么此时anth[i][j]可以接收栈顶天线的信号，比如5 3 2 3，最后一个3可以接收到前面等高3的信号，但是无法继续接收前面5的信号，因此这里anth[i][j]结束处理
        if anth[i][j] == stack[-1]:
            ret[i][j] += 1
            stack.pop()  # 维护严格递减栈
        # 此情况必然是：anth[i][j] < stack.at(-1)，那么此时anth[i][j]可以接收栈顶天线的信号，比如6 5 2 3，最后一个3可以接收到前面5的信号，但是无法继续接收更前面6的信号，因此这里anth[i][j]结束处理
        else:
            ret[i][j] += 1
    stack.append(anth[i][j])


# 算法源码
def getResult(m, n, arr):
    anth = [[0 for j in range(n)] for i in range(m)]

    for i in range(m * n):
        r = int(i / n)
        c = i % n
        anth[r][c] = arr[i]

    ret = [[0 for j in range(n)] for i in range(m)]

    # 先处理东向发射信号
    for i in range(m):
        stack = []
        for j in range(n):
            common(stack, anth, ret, i, j)

    # 再处理南向发射信号
    for j in range(n):
        stack = []
        for i in range(m):
            common(stack, anth, ret, i, j)

    res = " ".join([" ".join(map(str, i)) for i in ret])

    print(f'{m} {n}\n{res}')


# 算法调用
getResult(m, n, arr)
