# 对称字符串

def check(a: int, b: int):
    l = 1
    for _ in range(a - 1):
        l *= 2
    if a == 1 and b == 0:
        is_blue = False
        return is_blue
    else:
        x = b + 1
        if x > l / 2:
            is_blue = check(a - 1, b - l / 2)
        else:
            is_blue = not check(a - 1, b)
        return is_blue


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    color = check(a, b)
    if not color:
        print("red")
    else:
        print("blue")
