# 箱子之型摆放
import math

text, w = input().split()
w = int(w)

cols = [''] * math.ceil(len(text) / w)

for i in range(len(text)):
    num_c = i // w
    if num_c % 2 == 0:
        cols[num_c] += text[i]
    else:
        cols[num_c] = text[i] + cols[num_c]

# handle the case, the last line is backward and is not full.
if len(cols) % 2 == 0 and len(cols[-1]) != w:
    cols[-1] = (w - len(cols[-1])) * ' ' + cols[-1]

result = [''] * w

for i in range(w):
    for col in cols:
        if i < len(col) and col[i] != ' ':
            result[i] += col[i]
for res in result:
    if res == '':
        continue
    print(res)
