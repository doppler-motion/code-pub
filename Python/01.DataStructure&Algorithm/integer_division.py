class Solution:
    def divide(self, a: int, b: int) -> int:
        if (a >= 0 and b >= 0) or (a < 0 and b < 0):
            flag = False
        else:
            flag = True
        a, b = abs(a), abs(b)
        res = 0
        while a >= b:
            n = 1
            t = b
            while a > (t << 1):
                n <<= 1
                t <<= 1
            a -= t
            res += n
        if flag:
            res = -res

        return res if -2**31 <= res <= 2**31 - 1 else 2**31 - 1


if __name__ == "__main__":
    pass
