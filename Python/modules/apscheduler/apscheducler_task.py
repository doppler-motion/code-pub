import datetime
import time
from datetime import date
import os
import threading
import pytz

from apscheduler.schedulers.blocking import BlockingScheduler  # 阻塞型的任务调度器
from apscheduler.schedulers.background import BackgroundScheduler  # 后台运行的任务调度器
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


TZ = pytz.timezone("Asia/Shanghai")


class TriggerManager(object):
    def __init__(self):
        pass

    @classmethod
    def interval_trigger(cls, conf):
        time_args = {"s": 0, "m": 0, "h": 0, "d": 0, "w": 0}
        time_unit = conf["timeUnit"]
        time_interval = conf["timeInterval"]
        time_args[time_unit] = time_interval

        return IntervalTrigger(seconds=time_args["s"],
                               minutes=time_args["m"],
                               hours=time_args["h"],
                               days=time_args["d"],
                               weeks=time_args["w"],
                               timezone=TZ)


def my_job1():
    print("my_job1 is running, Now is %s" % datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))


def job():
    print(f"job thread_id-{threading.get_ident()}, process_id-{os.getpid()}")
    time.sleep(50)


def block_scheduler_use():
    block_scheduler = BlockingScheduler()
    block_scheduler.add_job(my_job1, "interval", seconds=3)
    block_scheduler.start()


def background_scheduler_use():
    background_scheduler = BackgroundScheduler()

    # background_scheduler.add_job(my_job1, "interval", seconds=3)
    background_scheduler.add_job(my_job1, "cron", second=3)
    background_scheduler.start()

    try:
        while True:
            time.sleep(2)

    except(KeyboardInterrupt, SystemExit):
        background_scheduler.shutdown()
        print("Exit the job!")


def judge_run_way():
    """
    判断 job 是进程方式，还是线程方式
    :return:
    """
    job_defaults = {"max_instances": 30}
    executors = {
        "default": ThreadPoolExecutor(10),  # 默认线程数
        "processpool": ProcessPoolExecutor(4)  # 默认进程数
    }
    shed = BackgroundScheduler(timezone="MST", executors=executors, job_defaults=job_defaults)
    shed.add_job(job, "interval", id="3_second_job", seconds=3)
    shed.start()

    try:
        while True:
            print("main 1s")
            time.sleep(1)
    except(KeyboardInterrupt, SystemExit):
        shed.shutdown()
        print("Exit the job!")


if __name__ == "__main__":
    # block_scheduler_use()
    background_scheduler_use()
    # judge_run_way()
