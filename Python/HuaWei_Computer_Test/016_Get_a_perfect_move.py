# 获取完美走位
def com_num(a, s):
    if a == [0, 0, 0, 0]:
        return 0
    elif sum(a) == 1:
        return 1
    else:
        for i in range(sum(a), len(s) + 1):
            for x in range(len(s) - i + 1):
                tt = [0, 0, 0, 0]
                s_ = s
                for j in range(i):
                    if s_[x + j] == 'A':
                        tt[0] += 1
                    elif s_[x + j] == 'S':
                        tt[1] += 1
                    elif s_[x + j] == 'D':
                        tt[2] += 1
                    elif s_[x + j] == 'W':
                        tt[3] += 1
                for z in range(4):
                    if a[z] == 0:
                        tt[z] = 0
                if tt == a:
                    return i


s = input()
num = [0, 0, 0, 0]
ASDW = ['A', 'S', 'D', 'W']
B = []
res = 0
for i in range(len(s)):
    if s[i] == 'A':
        num[0] += 1
    elif s[i] == 'S':
        num[1] += 1
    elif s[i] == 'D':
        num[2] += 1
    else:
        num[3] += 1
a = [i - int(len(s) / 4) for i in num]
for i in range(4):
    if a[i] < 0:
        a[i] = 0

res = com_num(a, s)
print(res)
