from pprint import pprint


class Student:
    student_count = 0  # 类变量


def main():
    print(Student.__name__)

    # 取得类属性
    print(Student.student_count)
    print(getattr(Student, "student_count"))
    print(getattr(Student, "unknown", 10))  # 不存在的属性

    # 修改类属性的值
    Student.student_count = 89
    print(Student.student_count)
    setattr(Student, "student_count", 90)
    print(Student.student_count)

    Student.newattribute = "hello"  # 动态添加变量
    print(Student.newattribute)

    # 类的所有实例共享类变量
    s1 = Student()
    s2 = Student()
    Student.student_count = 0
    print(s1.student_count)
    print(s2.student_count)

    pprint(Student.__dict__)


if __name__ == "__main__":
    main()
