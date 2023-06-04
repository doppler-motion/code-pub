import datetime
import threading
import os

from loguru import logger
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_MISSED, EVENT_JOB_MAX_INSTANCES, EVENT_ALL_JOBS_REMOVED, \
    EVENT_JOB_ADDED, EVENT_JOB_REMOVED, EVENT_JOB_MODIFIED, EVENT_JOB_EXECUTED, EVENT_JOB_SUBMITTED
from flask_apscheduler.scheduler import APScheduler, LOGGER
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'q5En7wAHpP8jsR^B6xnTP@ZEtWntV^FbV&JcQhU6Dg$ZNjPDEPC%qTZc0Q7llROE'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    # apscheduler默认的jobstore
    SCHEDULER_JOBSTORES = {}
    # flask_apscheduler是否对外提供接口
    SCHEDULER_API_ENABLED = True

    @classmethod
    def init_app(cls, app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+pymysql://root:123456qa!@127.0.0.1:3306/flaskdb?charset=utf8mb4'
    SCHEDULER_JOBSTORES = {"default": SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)}


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+pymysql://root:123456qa!@127.0.0.1:3306/flaskdb?charset=utf8mb4'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


class ApschedulerJobInfo(db.Model):
    """
        apscheduler job 定义表
    """
    JOB_STATUS_MAPPING = {
        0: "待执行",
        1: "执行完成",
        2: "执行异常",
        3: "未执行结束",
        4: "系统异常",
        5: "已删除",
        6: "批量删除"
    }

    # 应对历史的job名字映射 函数映射文字
    COMMON_JOB_NAME_MAPPING = {
        "end_before_2hours_notice": "拍卖结束前通知用户",
        "end_auction": "拍卖结束",
        "end_type1_auction": "直播拍卖结束",
        "auction_type1_start_product": "直播拍卖开始",
        "auction_preview_notify": "拍卖预展通知",
        "live_auction_start_notify": "拍卖开拍前提醒",
        "notify_ws": "拍卖开始",
        "heart_beat": "心跳任务",
    }

    __tablename__ = "apscheduler_job_info"
    id = db.Column(db.Integer, primary_key=True, comment="id 主键，用于防止JObID多次使用的情况")
    job_id = db.Column(db.String(200), nullable=False, comment="JOBID")
    job_name = db.Column(db.String(200), comment="JOB名字")
    job_trigger = db.Column(db.String(30), comment="触发类型")
    job_func = db.Column(db.String(200), comment="执行的函数信息")
    job_next_run_time = db.Column(db.String(30), comment="JOB下次执行时间")
    job_status = db.Column(db.Integer, nullable=False,
                           comment="JOB 状态 0:待执行 1:执行完成 2:执行异常 3:未执行结束 4:系统异常 5:已删除 6:批量删除")
    job_traceback = db.Column(db.TEXT, comment="执行报错时的错误信息")
    # create_time = db.Column(db.TIMESTAMP(True), nullable=True, comment="创建时间")
    # update_time = db.Column(db.TIMESTAMP(True), nullable=False, comment="更新时间")

    def __repr__(self):
        return self.job_id


class ApschedulerJobEventInfo(db.Model):
    """
        apscheduler job 事件表
    """
    EVENT_MAPPING = {
        0: "添加JOB",
        1: "修改JOB",
        2: "提交JOB",
        3: "执行JOB",
        4: "删除JOB",
        5: "执行JOB异常",
        6: "执行JOB过期",
        7: "全量删除JOB",
        8: "JOB超过最大实例数"
    }

    __tablename__ = "apscheduler_job_event_info"
    id = db.Column(db.Integer, primary_key=True, comment="id 主键，用于防止JObID多次使用的情况")
    job_info_id = db.Column(db.Integer, db.ForeignKey('apscheduler_job_info.id'), comment="JOB_INFO_ID")
    job_info = db.relationship("ApschedulerJobInfo", backref='events')
    event = db.Column(db.Integer,
                      comment="JOB事件 0:添加JOB 1:修改JOB 2:提交JOB 3:执行JOB 4:删除JOB 5:执行JOB异常 6:执行JOB过期 7:全量删除JOB 8:JOB超过最大实例数")
    # create_time = db.Column(db.TIMESTAMP(True), nullable=True, comment="创建时间")

    def __repr__(self):
        return "<<job:{} event:{}>>".format(self.job_info.job_id, self.EVENT_MAPPING.get(self.event, self.event))


class CustomAPScheduler(APScheduler):
    # scheduler事件映射本地状态
    STATUS_MAPPING = {
        EVENT_JOB_ADDED: 0,
        EVENT_JOB_MODIFIED: 1,
        EVENT_JOB_SUBMITTED: 2,
        EVENT_JOB_EXECUTED: 3,
        EVENT_JOB_REMOVED: 4,
        EVENT_JOB_ERROR: 5,
        EVENT_JOB_MISSED: 6,
        EVENT_ALL_JOBS_REMOVED: 7,
        EVENT_JOB_MAX_INSTANCES: 8
    }

    def __init__(self, session, scheduler=None, app=None):
        super(CustomAPScheduler, self).__init__(scheduler, app)
        self.session = session

    def listener_all_job(self, event):
        """
        监控job的生命周期，可视化监控，并且可增加后续的没有触发任务等监控
        添加到线程做处理
        :param event:
        :return:
        """
        job_id = None
        args = []
        if event.code != EVENT_ALL_JOBS_REMOVED:
            job_id = event.job_id
        if job_id:
            jobstore_alias = event.jobstore
            job = self.scheduler.get_job(job_id, jobstore_alias)
            if job:
                name = job.name
                func = str(job.func_ref)
                trigger = job.trigger if isinstance(job.trigger, str) else str(job.trigger).split("[")[0]
                next_run_time = str(job.next_run_time).split(".")[0]
            else:
                name = None
                func = None
                trigger = None
                next_run_time = None
            args = [name, func, trigger, next_run_time]
        traceback = event.traceback if hasattr(event, 'traceback') else "",
        args.append(traceback)
        t = threading.Thread(target=self.handle_listener_all_job, args=[event.code, job_id, *args])
        t.start()
        t.join()

    def handle_listener_all_job(self, event_type, *args):
        """
        实际处理IO操作
        如何处理一个job_id重复使用的问题，采用本地id自增，如果真有job_id重复的情况，则认为指定的是最后一个job_id对应的任务
        """
        try:
            if event_type == EVENT_JOB_ADDED:
                # 添加任务定义表
                job = ApschedulerJobInfo()
                job.job_id = args[0]
                job.job_name = args[1]
                job.job_func = args[2]
                job.job_trigger = args[3]
                job.job_next_run_time = args[4]
                job.job_status = 0
                # job.create_time = datetime.datetime.now()
                # job.update_time = datetime.datetime.now()
                self.session.add(job)
                self.session.flush()
                # 增加任务事件表
                job_event = ApschedulerJobEventInfo()
                job_event.job_info_id = job.id
                job_event.event = self.STATUS_MAPPING[event_type]
                # job_event.create_time = datetime.datetime.now()
                self.session.add(job_event)
                self.session.commit()
            elif event_type == EVENT_JOB_MODIFIED:
                # 修改job[取数据库表中job_id最后一个进行修改]
                job = ApschedulerJobInfo.query.order_by(ApschedulerJobInfo.id.desc()).filter(
                    ApschedulerJobInfo.job_id == args[0]).first()
                if job:
                    # 更新JOB表
                    job.job_name = args[1]
                    job.job_func = args[2]
                    job.job_trigger = args[3]
                    job.job_next_run_time = args[4]
                    job.job_status = 0

                    # 增加任务事件表
                    job_event = ApschedulerJobEventInfo()
                    job_event.job_info_id = job.id
                    job_event.event = self.STATUS_MAPPING[event_type]
                    self.session.add(job_event)
                    self.session.commit()
                else:
                    LOGGER.warning("指定的job本地不存在{}".format(args))
            elif event_type == EVENT_JOB_SUBMITTED:
                # 提交job执行
                job = ApschedulerJobInfo.query.order_by(ApschedulerJobInfo.id.desc()).filter(
                    ApschedulerJobInfo.job_id == args[0]).first()
                if job:
                    # 增加任务事件表
                    job_event = ApschedulerJobEventInfo()
                    job_event.job_info_id = job.id
                    job_event.event = self.STATUS_MAPPING[event_type]
                    self.session.add(job_event)
                    self.session.commit()
                else:
                    LOGGER.warning("指定的job本地不存在{}".format(args))
            elif event_type == EVENT_JOB_EXECUTED:
                # 执行job
                job = ApschedulerJobInfo.query.order_by(ApschedulerJobInfo.id.desc()).filter(
                    ApschedulerJobInfo.job_id == args[0]).first()
                if job:
                    # 更新JOB表
                    job.job_status = 1

                    # 增加任务事件表
                    job_event = ApschedulerJobEventInfo()
                    job_event.job_info_id = job.id
                    job_event.event = self.STATUS_MAPPING[event_type]
                    self.session.add(job_event)
                    self.session.commit()
                else:
                    LOGGER.warning("指定的job本地不存在{}".format(args))
            elif event_type == EVENT_JOB_REMOVED:
                # 删除job
                job = ApschedulerJobInfo.query.order_by(ApschedulerJobInfo.id.desc()).filter(
                    ApschedulerJobInfo.job_id == args[0]).first()
                if job:
                    # 更新JOB表
                    job.job_status = 5

                    # 增加任务事件表
                    job_event = ApschedulerJobEventInfo()
                    job_event.job_info_id = job.id
                    job_event.event = self.STATUS_MAPPING[event_type]
                    self.session.add(job_event)
                    self.session.commit()
                else:
                    LOGGER.warning("指定的job本地不存在{}".format(args))
            elif event_type == EVENT_JOB_ERROR:
                # 执行job出错
                job = ApschedulerJobInfo.query.order_by(ApschedulerJobInfo.id.desc()).filter(
                    ApschedulerJobInfo.job_id == args[0]).first()
                if job:
                    # 更新JOB表
                    job.job_status = 2
                    job.job_traceback = args[5]
                    # 增加任务事件表
                    job_event = ApschedulerJobEventInfo()
                    job_event.job_info_id = job.id
                    job_event.event = self.STATUS_MAPPING[event_type]
                    self.session.add(job_event)
                    self.session.commit()
                else:
                    LOGGER.warning("指定的job本地不存在{}".format(args))
            elif event_type == EVENT_JOB_MISSED:
                # job执行错过
                job = ApschedulerJobInfo.query.order_by(ApschedulerJobInfo.id.desc()).filter(
                    ApschedulerJobInfo.job_id == args[0]).first()
                if job:
                    # 更新JOB表
                    job.job_status = 3
                    job.job_traceback = args[5]
                    # 增加任务事件表
                    job_event = ApschedulerJobEventInfo()
                    job_event.job_info_id = job.id
                    job_event.event = self.STATUS_MAPPING[event_type]
                    self.session.add(job_event)
                    self.session.commit()
                else:
                    LOGGER.warning("指定的job本地不存在{}".format(args))
            elif event_type == EVENT_ALL_JOBS_REMOVED:
                # 删除所有job
                all_jobs = ApschedulerJobInfo.query.filter(ApschedulerJobInfo.job_status == 0).all()
                for job in all_jobs:
                    job.job_status = 6
                    # 增加任务事件表
                    job_event = ApschedulerJobEventInfo()
                    job_event.job_info_id = job.id
                    job_event.event = self.STATUS_MAPPING[event_type]
                    self.session.add(job_event)
                    self.session.commit()
            elif event_type == EVENT_JOB_MAX_INSTANCES:
                # job超过最大实例
                job = ApschedulerJobInfo.query.order_by(ApschedulerJobInfo.id.desc()).filter(
                    ApschedulerJobInfo.job_id == args[0]).first()
                if job:
                    # 更新JOB表
                    job.job_status = 4
                    job.job_traceback = args[5]
                    # 增加任务事件表
                    job_event = ApschedulerJobEventInfo()
                    job_event.job_info_id = job.id
                    job_event.event = self.STATUS_MAPPING[event_type]
                    self.session.add(job_event)
                    self.session.commit()
                else:
                    LOGGER.warning("指定的job本地不存在{}".format(args))
        except:
            LOGGER.exception("执行任务异常")

    def init_app(self, app):
        super(CustomAPScheduler, self).init_app(app)

        # 增加监听函数，监听所有job的生命周期
        self.add_listener(self.listener_all_job,
                          EVENT_JOB_ERROR | EVENT_JOB_MISSED | EVENT_JOB_MAX_INSTANCES | EVENT_ALL_JOBS_REMOVED | EVENT_JOB_ADDED | EVENT_JOB_REMOVED | EVENT_JOB_MODIFIED | EVENT_JOB_EXECUTED | EVENT_JOB_SUBMITTED)


# class Config(object):
#     JOBS = [
#         {
#             "id": "job1",
#             "func": "__main__:data_test",
#             "args": "",
#             "trigger": {
#                 "type": "cron",
#                 "day_of_week": "mon-fri",
#                 "hour": "0-23",
#                 "second": "*/5"
#             }
#         }
#     ]
#
#     SCHEDULER_API_ENABLED = True


app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


def data_test():
    print("I am working : %s" % (datetime.datetime.now()))


if __name__ == "__main__":
    config_name = os.getenv("FLASK_CONFIG") or "default"
    logger.info(config_name)

    # scheduler = APScheduler()
    print("Let us run out of loop!")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.app = app
    db.init_app(app)
    db.create_all()
    flask_apscheduler = CustomAPScheduler(db.session, app=app)
    flask_apscheduler.start()
    # scheduler.init_app(app)
    # scheduler.start()

    app.run(debug=False)
