import time


class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start_time = int(time.time())
        # self.start_time = time.perf_counter()  # cpu时钟
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = int(time.time())
        # self.end_time = time.perf_counter()
        self.elapsed = self.end_time - self.start_time
        return False


with Timer() as timer:
    print("test")
    time.sleep(3)
    print("end")

print(timer.elapsed)

