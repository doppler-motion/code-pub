class Person:
    def __init__(self):
        self.name = "Jack"


class Student(Person):
    def __init__(self, age):
        super().__init__()
        self.age = age


def main():
    student = Student(age=1)
    print(student.age)
    print(student.name)

    print(isinstance(student, Person))
    print(isinstance(student, Student))


if __name__ == "__main__":
    main()
