# 获取最大版本号
import re


def split(v):
    list1 = re.split('[.-]', v)
    for i in range(len(list1)):
        if i < 3:
            if list1[i] == '0':
                list1[i] = 0
            else:
                list1[i] = int(list1[i].lstrip('0'))
    return list1


v1 = input()
v2 = input()
list1 = split(v1)
list2 = split(v2)
# print(list1, list2)
i = 0
l1 = len(list1)
l2 = len(list2)
for i in range(4):
    if l1 < i + 1 or l2 < i + 1:
        if l1 != l2:
            max_v = v1 if l1 > l2 else v2
            print(max_v)
        else:
            print(v1)
            break
    if list1[i] > list2[i]:
        print(v1)
        break
    elif list1[i] < list2[i]:
        print(v2)
        break
