# 不含101的数
import sys

if __name__ == "__main__":
    def judge(n):
        if '101' in bin(n):
            return True
        else:
            return False


    tmp = sys.stdin.readline().strip().split()
    l, r = int(tmp[0]), int(tmp[1])
    # l,r=1,10
    result = 0
    i = l
    while i <= r:
        if i % 2 == 0:
            if judge(i):
                i += 2
            else:
                result += 1
                i += 1
                if bin(i)[-3:] != '101': result += 1
                i += 1
        else:
            if not judge(i): result += 1
            i += 1

    print(result)
