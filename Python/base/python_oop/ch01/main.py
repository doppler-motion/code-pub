class Student:
    pass


class Person:
    pass


def main():
    print(Student())
    # 类本身也是对象，是 type 类的对象
    print(type(Student))
    print(type(Person))

    student_1 = Student()
    print(student_1)
    print(hex(id(student_1)))  # 实例的地址

    print(isinstance(student_1, Student))  # 判断是否是Student类


if __name__ == "__main__":
    main()
