from pprint import pprint


class Student:
    student_count = 0  # 类变量

    # 初始化函数
    def __init__(self, name, age):
        self.name = name  # 实例变量
        self.age = age

    # 实例函数
    def say_hello(self, msg):
        print(f"hello {msg}, {self.name}")


def main():
    # 1. create a physical object
    # 2. call __init__() to initialize this object
    s1 = Student("Jac", 10)
    s2 = Student("Tom", 11)
    print(s1.student_count)
    print(s1.say_hello("1111"))
    print(s2.say_hello("2222"))

    # 动态定义实例属性(不共享)
    s1.gender = "Male"
    print(s1.gender)
    # print(s2.gender)  # 会报错


if __name__ == "__main__":
    main()
