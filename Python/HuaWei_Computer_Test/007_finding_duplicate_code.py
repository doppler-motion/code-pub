# 查找重复代码
text1, text2 = input().strip(), input().strip()
if len(text1) > len(text2): text1, text2 = text2, text1

head, tail = 0, 0
flag = 0
res = ''
while tail < len(text1):
    if text1[head:tail + 1] in text2:
        if tail - head + 1 > flag:
            flag = tail - head + 1
            res = text1[head:tail + 1]
        tail += 1
    else:
        head += 1
        tail = head
print(res)
