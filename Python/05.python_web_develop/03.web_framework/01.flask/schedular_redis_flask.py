import json
import os
import threading
import time
import uuid

from flask import Flask, jsonify, request
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED, EVENT_JOB_MISSED, EVENT_JOB_ADDED

from loguru import logger

app = Flask(__name__)


def work(num):
    start_time = int(time.time() * 1000)
    time.sleep(num)
    end_time = int(time.time() * 1000)
    logger.info(f"task end, cost 4.time : {end_time - start_time}")


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


sch_client = apscheduler_init()
sch_client.start()


@app.route("/")
def hello():
    return "hello world!"


@app.route("/add_job", methods=["POST", "GET"])
def add_job():
    """
    {
        "task_id": "",
        "num": 1,
        "4.time": 2
    }
    :return:
    """
    ret = {
        "msg": ""
    }
    try:
        logger.info(f"add_job() -> Accept request {request.json}")
        data = json.loads(request.json)
        task_id = data.get("task_id")
        num = data.get("num")
        interval_time = data.get("4.time")

        # 根据接口类型，添加任务
        sch_client.add_job(
            work,  # 执行任务的函数
            trigger="interval",  # 任务执行频次
            seconds=interval_time,
            jobstore="redis",  # 任务存储的对象
            id=task_id,  # 任务id
            args=[num],  # 函数的参数
            misfire_grace_time=60,  # 超过预计时间60秒，不再执行

        )
        logger.info("add task success!")
        ret["msg"] = "ok"
    except Exception as ex:
        logger.error(f"add_job() -> error: {ex}")
        ret["msg"] = str(ex)

    return jsonify(ret)


@app.route("/delete_job", methods=["POST", "GET"])
def delete_job():
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
        logger.info(f"delete_job() -> Accept request {request.json}")
        data = json.loads(request.json)
        task_id = data.get("task_id")
        # 根据接口类型，添加任务
        sch_client.remove_job(job_id=task_id, jobstore="redis")

        logger.info("delete task success!")
        ret["msg"] = "ok"
    except Exception as ex:
        logger.error(f"delete_job() -> error: {ex}")
        ret["msg"] = str(ex)
    return jsonify(ret)


@app.route("/delete_all_job", methods=["POST", "GET"])
def delete_all_job():
    """
    {
        "flag": 1,
    }
    :return:
    """
    ret = {
        "msg": ""
    }
    try:
        logger.info(f"delete_all_job() -> Accept request {request.json}")
        data = json.loads(request.json)
        flag = data.get("flag")
        if flag:
            # 删除所有任务
            sch_client.remove_all_jobs(jobstore="redis")

        logger.info("delete all task success!")
        ret["msg"] = "ok"
    except Exception as ex:
        logger.error(f"delete_all_job() -> error: {ex}")
        ret["msg"] = str(ex)
    return jsonify(ret)


@app.route("/pause_job", methods=["POST", "GET"])
def pause_job():
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
        logger.info(f"pause_job() -> Accept request {request.json}")
        data = json.loads(request.json)
        task_id = data.get("task_id")
        # 暂停任务
        sch_client.pause_job(job_id=task_id, jobstore="redis")

        logger.info("pause task success!")
        ret["msg"] = "ok"
    except Exception as ex:
        logger.error(f"pause_job() -> error: {ex}")
        ret["msg"] = str(ex)
    return jsonify(ret)


@app.route("/resume_job", methods=["POST", "GET"])
def resume_job():
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
        logger.info(f"resume_job() -> Accept request {request.json}")
        data = json.loads(request.json)
        task_id = data.get("task_id")
        # 重启任务
        sch_client.resume_job(job_id=task_id, jobstore="redis")

        logger.info("resume task success!")
        ret["msg"] = "ok"
    except Exception as ex:
        logger.error(f"resume_job() -> error: {ex}")
        ret["msg"] = str(ex)
    return jsonify(ret)


@app.route("/modify_job", methods=["POST", "GET"])
def modify_job():
    """
    {
        "task_id": "",
        "num": 1,
        "4.time": 2
    }
    :return:
    """
    ret = {
        "msg": ""
    }
    try:
        logger.info(f"modify_job() -> Accept request {request.json}")
        data = json.loads(request.data)
        task_id = data.get("task_id")
        interval_time = data.get("4.time")
        num = data.get("num")
        # 编辑任务, modify_job 这个方法不太熟，而且可能会有问题，故不采用这种方式
        # sheduler_trigger = sch_client._create_trigger(
        #     trigger="interval",
        #     trigger_args={"seconds": interval_time}
        # )
        # sch_client.modify_job(job_id=task_id, trigger=sheduler_trigger, jobstore="redis", args=[num])

        # 先删除任务
        sch_client.remove_job(job_id=task_id, jobstore="redis")
        # 然后创建新的任务
        sch_client.add_job(
            work,  # 执行任务的函数
            trigger="interval",  # 任务执行频次
            seconds=interval_time,
            jobstore="redis",  # 任务存储的对象
            id=task_id,  # 任务id
            args=[num],  # 函数的参数
            misfire_grace_time=60,  # 超过预计时间60秒，不再执行
        )
        logger.info("modify task success!")
        ret["msg"] = "ok"
    except Exception as ex:
        logger.error(f"modify_job() -> error: {ex}")
        ret["msg"] = str(ex)
    return jsonify(ret)


@app.route("/get_jobs", methods=["POST", "GET"])
def get_jobs():
    logger.info(f"get_jobs() -> Accept request {request.json}")
    data = json.loads(request.data)
    flag = data.get("flag")
    # 根据接口类型，添加任务
    job_list = sch_client.get_jobs()
    logger.info("job list: ", job_list)
    job_infos = {}
    for job in job_list:
        job_id = job.id
        job_infos[job_id] = {}
        job_infos[job_id]["name"] = job.name
        job_infos[job_id]["next_run_time"] = job.next_run_time

    return jsonify({"msg": "ok", "data": job_infos})


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=5005, debug=False)
    # sch_client.add_job(work, "interval", seconds=5, args=[4.time.4.time()])
    # sch_client.start()
    # while True:
    #     4.time.sleep(2)
    logger.info(dir(EVENT_JOB_ADDED))
