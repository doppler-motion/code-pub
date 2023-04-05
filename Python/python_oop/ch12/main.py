class Person:
    color = 1

    def __init__(self):
        self.name = "Jack"

    def say(self):
        print("hello from person")

    def print_color(self):
        print(self.color)


class Student(Person):
    color = 2

    def __init__(self, age):
        super().__init__()
        self.age = age

    def say(self):
        print("hello from student")


class Worker(Person):
    pass


def render(person: Person):
    person.say()


def main():
    student = Student(age=1)
    student.say()

    person = Person()
    person.say()

    render(student)
    render(Worker())

    print(student.color)
    student.print_color()


if __name__ == "__main__":
    main()
