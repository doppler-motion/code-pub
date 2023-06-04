from apscheduler.triggers.interval import IntervalTrigger
# from apscheduler.triggers.cron import CronTrigger

from loguru import logger

from .worker import Worker, work

func_map = {
    "class_func": Worker,
    "normal_func": work,
}


class JobManage:
    def __init__(self):
        self.client = None
        self.task_id = None

        self.func = None
        self._config = None
        self.dict_config = None
        self.jobstore = "redis"
        self.trigger = None
        self.misfire_grace_time = 60

    def add_task(self):
        self.client.add_job(func=self.func,
                            args=self._config,
                            kwargs=self.dict_config,
                            id=self.task_id,
                            name=self.task_id,
                            jostore=self.jobstore,
                            trigger=self.trigger,
                            misfire_grace_time=self.misfire_grace_time,
                            )
        logger.info("[ execute ] add task success!")

    def delete_task(self):
        self.client.remove_job(job_id=self.task_id, jobstore=self.jobstore)
        logger.info("[ execute ] delete task success!")

    def pause_task(self):
        self.client.pause_job(job_id=self.task_id, jobstore=self.jobstore)
        logger.info("[ execute ] pause task success!")

    def resume_task(self):
        self.client.resume_job(job_id=self.task_id, jobstore=self.jobstore)
        logger.info("[ execute ] resume task success!")

    def pause_client(self):
        self.client.pause()
        logger.info("[ execute ] pause client success!")

    def resume_client(self):
        self.client.resume()
        logger.info("[ execute ] resume client success!")

    def remove_all_task(self):
        self.client.remove_all_job(jobstore=self.jobstore)
        logger.info("[ execute ] remove all task success!")


class TaskManager(JobManage):
    def __init__(self):
        JobManage.__init__(self)

        self.funcs = {}
        self.action = None

        self.__funcs()

        logger.info("[ execute ] init task manager success!")

    def manage_task(self, **kwargs):
        self.task_id = kwargs.get("task_id")
        self.action = kwargs.get("action")

        self.func = func_map.get(kwargs.get("func"))
        self.dict_config = kwargs.get("dict_config")
        self._config = kwargs.get("_config")

        self.trigger = IntervalTrigger(seconds=30)

        _execute_func = self.funcs.get(self.action)
        _execute_func()

    def __funcs(self):
        self.funcs = {
            "add": self.add_task,
            "delete": self.delete_task,
            "pause": self.pause_task,
            "resume": self.resume_task,
            "pause_all": self.pause_client,
            "resume_all": self.resume_client,
            "remove_all": self.remove_all_task,
        }
