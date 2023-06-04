import time

from loguru import logger


class Worker:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.num = self.kwargs.get("num")

        self.main()

    def main(self):
        start_time = int(time.time() * 1000)
        time.sleep(self.num)
        end_time = int(time.time() * 1000)
        logger.info(f"task end, cost time : {end_time - start_time}")


def work(num):
    start_time = int(time.time() * 1000)
    time.sleep(num)
    end_time = int(time.time() * 1000)
    logger.info(f"task end, cost time : {end_time - start_time}")
