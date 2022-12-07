# 创建生成器

# 第1种方法 将列表生成器的[] 换为 ()
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)


# 第2种方法 函数定义中包含yield关键字
def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        yield b
        a, b = b, a + b
        n += 1
    return "Done"
