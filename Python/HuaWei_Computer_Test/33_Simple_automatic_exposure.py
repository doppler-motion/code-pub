# 简单的自动曝光

import sys


def solve_method(line):
    k = 0
    img = list(map(int, line.split()))
    avg = sum(img) // len(img)

    diff = avg - 128
    new_img = img.copy()
    if diff > 0:
        while avg > 127:
            k -= 1
            avg = update_and_get_avg(new_img, -1)
    if diff < 0:
        while avg < 128:
            k += 1
            avg = update_and_get_avg(new_img, 1)
    return k


def update_and_get_avg(new_img, lambda_):
    for i in range(len(new_img)):
        if new_img[i] + lambda_ > 255:
            new_img[i] = 255
        elif new_img[i] + lambda_ < 0:
            new_img[i] = 0
        else:
            new_img[i] += lambda_
    return sum(new_img) // len(new_img)


def main():
    line = sys.stdin.readline()
    res = solve_method(line)
    print(res)


if __name__ == '__main__':
    main()
