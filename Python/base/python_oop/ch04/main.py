from pprint import pprint


class Student:
    student_count = 0  # 类变量

    # 初始化函数
    def __init__(self, name):
        self._name = name  # 实例变量, 私有属性, 外部亦可访问
        self.__name = name  # 实例变量, 私有属性， 外部不能访问

    # 实例函数
    def say_hello(self, msg):
        print(f"hello {msg}, {self.__name}")


def main():
    s1 = Student("Jack")
    print(s1._name)  # 可打印
    # print(s1.__name)  # 报错，调用方法 _classname__attribute
    print(s1._Student__name)


if __name__ == "__main__":
    main()
