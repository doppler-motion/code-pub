# 核酸检测人员安排

import functools


def comp(a, b):
    return b - a


if __name__ == "__main__":
    params = [int(x) for x in input().split(" ")]
    sample_num = params[0]
    volunteer_num = params[1]
    efficiencys = [int(x) for x in input().split(" ")]

    # 按效率排序，因为要先给效率最高的采样员配备志愿者
    efficiencys = sorted(efficiencys, key=functools.cmp_to_key(comp))

    result = 0
    # 每个采样员配备的志愿者个数
    count = 0
    # 分别指向效率最高的采样员和效率最低的采样员，以便后续进行志愿者重新分配
    i = 0
    j = 0

    # 分支1: 志愿者<采样员，优先将志愿者分配给效率高的采样员
    if volunteer_num < sample_num:
        for k in range(sample_num):
            if k < volunteer_num:
                result += efficiencys[k]
            else:
                result += efficiencys[k] * 0.8
        j = volunteer_num - 1
    # 分支2: 志愿者>=采样员，先给每个采样员都分配一个志愿者
    else:
        # 如果志愿者人数超过采样员四倍，则多出来的志愿者无效
        if volunteer_num >= 4 * sample_num:
            volunteer_num = 4 * sample_num

        for val in efficiencys:
            result += val
        # 多出来的志愿者
        remain_num = volunteer_num - sample_num
        j = sample_num - 1

        while remain_num > 0:
            result += efficiencys[i] * 0.1
            remain_num -= 1
            count += 1
            if count == 4:
                count = 0
                i += 1

    # 剥夺低效率采样员的志愿者给高效率的采样员
    while i < j:
        # 最高效率的采样员上升10%的效率 > 最低效率的采样员下降20%的效率
        if efficiencys[i] * 0.1 > efficiencys[j] * 0.2:
            result += efficiencys[i] * 0.1 - efficiencys[j] * 0.2

            # 最多就4个志愿者
            count += 1
            if count == 4:
                count = 0
                i += 1
            j -= 1
        else:
            break

    print(int(result))
