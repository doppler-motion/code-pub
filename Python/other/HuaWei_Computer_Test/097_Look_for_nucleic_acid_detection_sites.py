# 寻找核酸检测点
class Point:
    def __init__(self, idx, dis, que):
        self.idx = idx
        self.dis = dis
        self.que = que
        self.pay = dis * 10
        self.time = get_time(start, self)


add8_10 = [3, 480, 600]
add12_14 = [10, 720, 840]


def get_time(start, point):
    time = 0
    time += point.dis * 10
    point.que = max(0, point.que - point.dis * 10)
    on = start + point.dis * 10
    if on <= add8_10[1]:
        return add8_10[1] - start
    if on <= add8_10[2]:
        point.que += (on - add8_10[1]) * add8_10[0] - (on - add8_10[1])
        return time + point.que
    if on <= add12_14[1]:
        return time + point.que
    if on <= add12_14[2]:
        point.que += (on - add12_14[1]) * add12_14[0] - (on - add12_14[1])
        return time + point.que
    return time + point.que


def solve_method(start, end, points):
    res = [p for p in points if start + p.time < end]
    res.sort(key=lambda x: (x.time, x.pay))
    print(len(res))
    for p in res:
        print(p.idx, p.time, p.pay)


if __name__ == '__main__':
    t1 = input().strip().split(' ')
    start = int(t1[0]) * 60 + int(t1[1])
    t2 = input().strip().split(' ')
    end = int(t2[0]) * 60 + int(t2[1])

    n = int(input().strip())
    points = [Point(*map(int, input().strip().split())) for _ in range(n)]
    solve_method(start, end, points)
