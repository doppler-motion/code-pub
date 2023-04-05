def execute(*args, **kwargs):
    print(args)
    print(kwargs)


class SquareNumber(int):
    def __new__(cls, value: int):
        return super().__new__(cls, value ** 2)


class Student:
    def __new__(cls, first_name, last_name):
        obj = super().__new__(cls)
        obj.first_name = first_name
        obj.last_name = last_name
        return obj


def main():
    execute("abc")
    execute("abc", "def")
    execute("abc", 12)
    execute("abc", 12, name="java", age=10)

    num = SquareNumber(2)
    print(num)
    print(type(num))
    print(isinstance(num, int))

    student = Student("Jack", "Chen")
    print(student.last_name)
    print(student.first_name)


if __name__ == "__main__":
    main()
