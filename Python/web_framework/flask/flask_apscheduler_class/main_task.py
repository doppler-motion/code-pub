import json
import os, sys
import threading
import time
import uuid

from flask import Flask, jsonify, request
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED, EVENT_JOB_MISSED

from loguru import logger

from funcs.task_manager import TaskManager

app = Flask(__name__)


def job_listener(event):
    job = sch_client.get_job(event.job_id)
    if not event.exception:
        logger.info("jobname = %s|jobtrigger = %s|thread_id = %s"
                    "|process_id= %s |jobtime = %s|retval = %s|" % (job.name,
                                                                    job.trigger,
                                                                    threading.get_ident(),
                                                                    os.getpid(),
                                                                    event.scheduled_run_time,
                                                                    event.retval))
    else:
        logger.error("jobname = %s|jobtrigger = %s|errcode = %s"
                     "|exception= [%s] |traceback = [%s]|scheduled_time = %s" % (job.name,
                                                                                 job.trigger,
                                                                                 event.code,
                                                                                 event.exception,
                                                                                 event.traceback,
                                                                                 event.scheduled_run_time))


def apscheduler_init():
    redis_config = {
        "host": "127.0.0.1",
        "port": "6379",
        "db": 2,
        "password": "123456qa!",
        "jobs_key": "test",
        "run_times_key": "interval"
    }

    # 设置任务的存储位置为redis
    jobstores = {
        "redis": RedisJobStore(**redis_config),
        "default": MemoryJobStore()
    }

    # 设置定时任务的线程和进程，可选配置
    executors = {
        "default": ThreadPoolExecutor(10),  # 默认线程数
        "processpool": ProcessPoolExecutor(4)  # 默认进程
    }

    # 实例化定时任务对象，用于定时任务的添加，修改，删除等操作
    scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors)
    # 添加监听器
    scheduler.add_listener(job_listener, EVENT_JOB_MISSED | EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    return scheduler


@app.route("/")
def hello():
    return "hello world!"


@app.route("/manage_task", methods=["POST", "GET"])
def manage_task():
    """
    {
        "task_id": "",
    }
    :return:
    """
    ret = {
        "msg": ""
    }
    try:
        logger.info(f"manage_task() -> Accept request {request.json}")
        data = json.loads(request.data)
        logger.info(f"data: {data}")

        task_manager.manage_task(**data)

        logger.info("manage task success!")
        ret["msg"] = "ok"
    except Exception as ex:
        logger.error(f"manage_task() -> error: {ex}")
        ret["msg"] = str(ex)
    return jsonify(ret)


@app.route("/get_jobs", methods=["POST", "GET"])
def get_jobs():
    logger.info(f"get_jobs() -> Accept request {request.json}")
    data = json.loads(request.data)
    flag = data.get("flag")
    # 根据接口类型，添加任务
    job_list = sch_client.get_jobs()
    logger.info(f"job list: {job_list}")
    job_infos = {}
    for job in job_list:
        job_id = job.id
        job_infos[job_id] = {}
        job_infos[job_id]["name"] = job.name
        job_infos[job_id]["next_run_time"] = job.next_run_time

    return jsonify({"msg": "ok", "data": job_infos})


if __name__ == "__main__":
    while True:
        try:
            sch_client = apscheduler_init()
            sch_client.start()

            task_manager = TaskManager()
            task_manager.client = sch_client

            host, port = "127.0.0.1", 5005
            app.run(host=host, port=port, debug=False)
        except:
            logger.exception("main task run failed, will retry later!")
            time.sleep(30)
