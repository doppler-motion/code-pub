

# 在单继承中，super() 和 __init__() 功能类似，super() 不用显示引用基类
class Base(object):
    def __init__(self, name):
        self.name = name
        print("Base created.")

    def func(self):
        print("base func")


class ChildA(Base):
    def __init__(self):
        print("ChildA created.")
        Base.__init__(self, "A")  # 父类硬编码进子类中
    
    def funca(self):
        print("ChildA func.")


class ChildB(Base):
    def __init__(self):
        print("ChildB created.")
        super(ChildB, self).__init__("B")  # super进行父类初始化

    def funcb(self):
        print("ChildB func.")


A = ChildA()
B = ChildB()

