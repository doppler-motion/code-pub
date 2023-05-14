# 新员工座位安排系统
import sys

if __name__ == "__main__":
    line = sys.stdin.readline()
    F = line.split()
    n = len(F)
    try:
        if n < 1 or n > 100000:
            raise Exception
    except Exception:
        print('Error!')

    friend = dict()

    while ('0' in F):
        f = 0
        position = F.index('0')
        if position == None:
            break
        left = position - 1
        right = position + 1

        while (left >= 0):
            if F[left] == '1':
                f += 1
                left -= 1
            else:
                break
        while (right < n):
            if F[right] == '1':
                f += 1
                right += 1
            else:
                break
        friend[position] = f
        F[position] = 3

    value_list = list(friend.values())
    if value_list:
        max_value = max(value_list)
        print(max_value)
    else:
        print(0)
