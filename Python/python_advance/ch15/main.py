from threading import Thread


def func():
    for i in range(10):
        print(i)


thread1 = Thread(target=func, )
thread2 = Thread(target=func, )

thread1.start()
thread2.start()

thread1.join()
thread2.join()
