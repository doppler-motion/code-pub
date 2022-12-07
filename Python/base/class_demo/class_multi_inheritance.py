"""

多重继承中，super返回的是继承顺序的下一个类

"""

class Base(object):
    def __init__(self):
        print("Base created.")


class ChildA(Base):
    def __init__(self):
        print("init A")
        super(ChildA, self).__init__()
        # Base.__init__(self)
        print("init A end.")


class ChildB(Base):
    def __init__(self):
        print("init B")
        super(ChildB, self).__init__()
        print("init B end")


class ChildC(ChildA, ChildB):
    pass


# C = ChildC()


"""
以上执行结果解释：
子类C执行顺序：ChildA().init() -> ChildB().init() -> Base().init()
如果将A子类中的super换成__init__(),执行顺序ChildA().init() -> Base().init(), 跳过了B子类
"""


class childA(Base):
    def __init__(self):
        print("init A")
        # Base.__init__(self)
        super(childA, self).__init__()
        print("init A end.")


class childB(childA, Base):
    def __init__(self):
        print("init B")
        # childA.__init__(self)
        # Base.__init__(self)
        super(childB, self).__init__()

B = childB()


"""
以上输出结果解释：
super() 可以避免重复调用

子类B继承了基类Base()和子类A，
子类A初始化了基类Base，子类B初始化了子类A，也初始化了基类Base，导致基类初始化了两次

使用super()可以避免以上问题
"""
