def solve_method(seq, n):
    max_value = 0
    dp = seq[:]
    sum_count = {}
    sum_pos = {}

    for i in range(n):
        for j in range(n - i):
            if i > 0:
                dp[j] += seq[j + i]
            sum_val = dp[j]
            if sum_val not in sum_count:
                sum_count[sum_val] = 0
                sum_pos[sum_val] = set()

            exists = False
            poss = sum_pos[sum_val]
            for k in range(j, j + i + 1):
                if k in poss:
                    exists = True
                    break
            if not exists:
                sum_count[sum_val] += 1
                max_value = max(max_value, sum_count[sum_val])
                for k in range(j, j + i + 1):
                    poss.add(k)
                sum_pos[sum_val] = poss

    return max_value


def main():
    n = int(input().strip())
    seq = list(map(int, input().strip().split()))
    res = solve_method(seq, n)
    print(res)


if __name__ == "__main__":
    main()
