# -*- coding: UTF-8 -*-
"""
# rs勿忘初心
"""
import threading
import time
import uuid
import redis

from loguru import logger

# redis连接
redis_client = redis.Redis(host="127.0.0.1",
                           port=6379,
                           db=8)


# 获取一个锁
# lock_name：锁定名称
# acquire_time: 客户端等待获取锁的时间
# time_out: 锁的超时时间
def acquire_lock(lock_name, acquire_time=3, time_out=5):
    """获取一个分布式锁"""
    identifier = str(uuid.uuid4())
    end = time.time() + acquire_time
    lock = "string:lock:" + lock_name
    while time.time() < end:
        if redis_client.setnx(lock, identifier):
            # 给锁设置超时时间, 防止进程崩溃导致其他进程无法获取锁
            redis_client.expire(lock, time_out)
            return identifier
        elif not redis_client.ttl(lock):
            redis_client.expire(lock, time_out)
        time.sleep(0.001)
    return False


# # 释放一个锁
# def release_lock(lock_name, identifier):
#     """通用的锁释放函数"""
#     lock = "string:lock:" + lock_name
#     pip = redis_client.pipeline(True)
#     while True:
#         try:
#             pip.watch(lock)
#             lock_value = redis_client.get(lock)
#             if not lock_value:
#                 return True
#
#             if lock_value.decode() == identifier:
#                 pip.multi()
#                 pip.delete(lock)
#                 pip.execute()
#                 return True
#             pip.unwatch()
#             break
#         except redis.excetions.WacthcError:
#             pass
#     return False


def release_lock(lock_name, identifier):
    """
    释放锁
    :param lock_name: 锁的名称
    :param identifier: 锁的标识
    :return:
    """
    global redis_client
    try:
        unlock_script = """
            if redis.call("get",KEYS[1]) == ARGV[1] then
                return redis.call("del",KEYS[1])
            else
                return 0
            end
            """
        lockname = f'lock:{lock_name}'
        unlock = redis_client.register_script(unlock_script)
        result = unlock(keys=[lockname], args=[identifier])
        if result:
            return True
        else:
            return False
    except:
        logger.warning("release redis lock failed!")
        return False


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def thread_func():
    while True:
        # 获取当前时间
        now_time = get_current_time().strip()
        # 判断是不是整分
        if now_time.split(":")[-1] == "00" or now_time.split(":")[-1] == "0":
            # 判断是不是获得锁
            redis_lock_identifier = acquire_lock("redis_lock_availability")
            if redis_lock_identifier:
                logger.info("thread get lock, begin to do some work")
                time.sleep(8)
                release_lock("redis_lock_availability", redis_lock_identifier)
            else:
                logger.info("thread not get lock, please wait next turn!")
        else:
            logger.info("thread please wait next turn!")
        # 等待下一轮
        end_time = get_current_time().strip().split(":")[-1]
        remain_time = 60 - int(end_time)
        time.sleep(remain_time)


def thread_func1():
    while True:
        # 获取当前时间
        now_time = get_current_time().strip()
        # 判断是不是整分
        if now_time.split(":")[-1] == "00" or now_time.split(":")[-1] == "0":
            # 判断是不是获得锁
            redis_lock_identifier = acquire_lock("redis_lock_availability")
            if redis_lock_identifier:
                logger.info("thread1 get lock, begin to do some work")
                time.sleep(8)
                release_lock("redis_lock_availability", redis_lock_identifier)
            else:
                logger.info("thread1 not get lock, please wait next turn!")
        else:
            logger.info("thread1 please wait next turn!")
        # 等待下一轮
        end_time = get_current_time().strip().split(":")[-1]
        remain_time = 60 - int(end_time)
        time.sleep(remain_time)


# def seckill(i):
#     identifier = acquire_lock('resource')
#     print("线程:{}--获得了锁".format(i))
#     time.sleep(1)
#     global count
#     if count < 1:
#         print("线程:{}--没抢到，票抢完了".format(i))
#         return
#     count -= 1
#     print("线程:{}--抢到一张票，还剩{}张票".format(i, count))
#     release_lock('resource', identifier)

if __name__ == "__main__":
    threading.Thread(target=thread_func, ).start()
    threading.Thread(target=thread_func1, ).start()
