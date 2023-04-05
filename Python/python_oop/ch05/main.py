class Student:
    school = "abc"

    @classmethod
    def hello(cls):
        print(f"hello {cls.__name__}")

    @staticmethod
    def out():
        print(f"hello {Student.school}")


def main():
    Student.hello()
    print(Student.__name__)

    Student.out()


if __name__ == "__main__":
    main()
