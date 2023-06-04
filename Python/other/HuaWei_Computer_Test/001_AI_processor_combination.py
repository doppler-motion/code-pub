# AI 处理器组合

cpu = []
string = input()
for ch in string:
    if ch.isdigit():
        cpu.append(ch)
cpu = list(map(int, cpu))
cpu = sorted(cpu)
num = int(input())
out = []


def is_duplicated(array, res):
    if len(array) == 2 * res:
        return True
    else:
        return False


def check(cpu, res):
    line1 = []
    line2 = []
    for i in cpu:
        if 0 <= i <= 3:
            line1.append(i)
        elif 4 <= i <= 7:
            line2.append(i)
    if len(line1) == len(line2):  # both have the same number
        if len(line1) == res:
            for i in range(len(line2)):
                line1.append(line2[i])
            return line1
    if len(line1) == res:
        return line1
    elif len(line2) == res:
        return line2
    else:
        return False


sub_cpu = 0
if num == 1:
    if check(cpu, 1):
        sub_cpu = check(cpu, 1)
    elif check(cpu, 3):
        sub_cpu = check(cpu, 3)
    elif check(cpu, 2):
        sub_cpu = check(cpu, 2)
    elif check(cpu, 4):
        sub_cpu = check(cpu, 4)
    else:
        print('[]')
    if sub_cpu:
        for i in sub_cpu:
            out.append([i])
        print(out)

if num == 2:
    if check(cpu, 2):
        sub_cpu = check(cpu, 2)
        if is_duplicated(sub_cpu, 2):
            for i in range(2):
                out.append(sub_cpu[i * 2:i * 2 + 2])
            print(out)
        else:
            out.append(sub_cpu)
            print(out)
    elif check(cpu, 4):
        sub_cpu = check(cpu, 4)
        if is_duplicated(sub_cpu, 4):
            for i in range(2):
                line = sub_cpu[4 * i: 4 * i + 4]
                for i in range(len(line)):
                    for j in range(i + 1, len(line)):
                        out.append([line[i], line[j]])
            print(out)
        else:
            for i in range(len(sub_cpu)):
                for j in range(i + 1, len(sub_cpu)):
                    out.append([sub_cpu[i], sub_cpu[j]])
            print(out)
    elif check(cpu, 3):
        sub_cpu = check(cpu, 3)
        if is_duplicated(sub_cpu, 3):
            for i in range(2):
                line = sub_cpu[3 * i: 3 * i + 3]
                for i in range(len(line)):
                    for j in range(i + 1, len(line)):
                        out.append([line[i], line[j]])
            print(out)
        else:
            for i in range(len(sub_cpu)):
                for j in range(i + 1, len(sub_cpu)):
                    out.append([sub_cpu[i], sub_cpu[j]])
            print(out)
    else:
        print('[]')

if num == 4:
    if check(cpu, 4):
        sub_cpu = check(cpu, 4)
        if is_duplicated(sub_cpu, 4):
            for i in range(2):
                line = sub_cpu[4 * i: 4 * i + 4]
                out.append(line)
            print(out)
        else:
            out.append(sub_cpu)
            print(out)
    else:
        print('[]')
if num == 8:
    if len(cpu) == 8:
        out.append(cpu)
        print(out)
    else:
        print('[]')
