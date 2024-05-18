# MVP争夺战
import sys


def dfs(arr, bucket, ind, ave):
    if ind == len(arr):
        return 1
    for i in range(len(bucket)):
        if bucket[i] + arr[ind] <= ave:
            bucket[i] += arr[ind]
            if (dfs(arr, bucket, ind + 1, ave)):
                return 1
            bucket[i] -= arr[ind]
    return 0


n = int(sys.stdin.readline().strip())
vec_list = sys.stdin.readline().strip().split(" ")
arr = list(map(int, vec_list))
vec_sum = sum(arr)
arr.sort()
hi = arr[-1]  # 取最大值


def do_job():
    for i in range(hi, vec_sum + 1):
        if vec_sum % i == 0:
            lev = int(vec_sum / i)
            bucket = []
            for j in range(lev):
                bucket.append(0)
            if (dfs(arr, bucket, 0, i)):
                print(i)
                break


if __name__ == "__main__":
    do_job()
