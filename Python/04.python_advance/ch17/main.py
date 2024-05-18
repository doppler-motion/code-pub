from threading import Thread, Lock, Condition

task_lock = Lock()


def func(name: str):
    for i in range(2):
        print(f"{name} - round {i} - step 1\n", end="")
        print(f"{name} - round {i} - step 2\n", end="")
        print(f"{name} - round {i} - step 3\n", end="")


t1 = Thread(target=func, args=("A",))
t2 = Thread(target=func, args=("B",))
t3 = Thread(target=func, args=("C",))

t1.start()
t2.start()
t3.start()


class SafeQueue:
    def __init__(self, size: int):
        self.__item_list = list()
        self.size = size

        self.__item_lock = Condition()

    def put(self, item):
        with self.__item_lock:
            while len(self.__item_list) >= self.size:
                self.__item_lock.wait()

            self.__item_list.insert(0, item)
            self.__item_lock.notify_all()

    def get(self):
        with self.__item_lock:
            while len(self.__item_list) == 0:
                self.__item_lock.wait()

            result = self.__item_list.pop()
            self.__item_lock.notify_all()

            return result
