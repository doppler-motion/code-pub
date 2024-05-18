import time


class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = time.perf_counter()  # 程序执行到此处时的cpu时钟
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        return False


with Timer() as timer:
    nums = []
    for n in range(10000):
        nums.append(n)
print(timer.elapsed)
