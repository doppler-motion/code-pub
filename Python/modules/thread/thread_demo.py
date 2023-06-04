import threading
import time

# 线程锁
lock = threading.Lock()
num_list = []


# 创建多线程方式1， 继承threading.Thread(), 重写其中的run()方法
class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self) -> None:
        print("线程要执行的内容： {}".format(self.num))

        time.sleep(3)


# 创建多线程方式2， 通过 threading.Thread()直接实例化, 参数是执行的函数，以及函数需要的参数
def func1(num):
    print(f"线程创建，编号： {num}")
    time.sleep(3)


# 测试线程锁 不加锁
def func_no_lock(n):
    num_list.append(n)
    print(num_list)


# 测试线程锁 加锁
def func_lock(n):
    lock.acquire()
    num_list.append(n)
    print(num_list)
    lock.release()


# 测试线程锁函数
def threading_lock_test():
    for num in range(10):
        th = threading.Thread(target=func_no_lock, args=(num, ))
        th.start()


if __name__ == "__main__":
    # 创建线程方法1
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
    #
    # # 创建线程方法2
    # for i in range(10):
    #     t1 = threading.Thread(target=func1, args=(i, ))
    #     t1.start()
    #
    # # 测试线程锁
    # threading_lock_test()
