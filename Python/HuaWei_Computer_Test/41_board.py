# 木板

n, m = [int(i) for i in input().split()]
lst = [int(i) for i in input().split()]
least = min(lst)
counts = lst.count(least)
while 1:
    # least = min(lst)
    # counts = lst.count(least)
    if m >= counts:
        m -= counts
        least += 1
        counts += lst.count(least)
    else:
        print(least)
        break
