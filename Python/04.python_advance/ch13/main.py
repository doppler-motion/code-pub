# 方法1
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance["cls"] = self._cls
        return self._cls


# 方法 2
# def singleton(cls):
#     print("step 1")
#
#     def inner(*args, **kwargs):
#         if hasattr(cls, "__instance"):
#             return getattr(cls, "__instance")
#
#         print("step 2")
#
#         obj = cls(*args, **kwargs)
#         setattr(cls, "__instance", obj)
#
#         return obj
#
#     return inner


# 方法 3 闭包
def singleton(cls):
    print("step 1")
    _instance = {}

    def inner(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]

        print("step 2")

        obj = cls(*args, **kwargs)
        _instance[cls] = obj

        return obj

    return inner


# 方法4 元类
class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        if hasattr(cls, "_instance"):
            return getattr(cls, "_instance")

        obj = super().__call__(*args, **kwargs)
        setattr(cls, "_instance", obj)
        return obj


# @Singleton
class Person(metaclass=SingletonMeta):
    pass


p1 = Person()
p2 = Person()

print(p1 is p2)  # 希望输出 True
