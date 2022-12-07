class MapMixin:
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


class DictMixin:
    def to_dict(self):
        return self.__convert_dict(self.__dict__)

    def __convert_dict(self, attrs: dict):
        result = {}
        for key, value in attrs.items():
            result[key] = self.__convert_value(value)

    def __convert_value(self, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self.__convert_dict(value)
        elif isinstance(value, list):
            return [self.__convert_value(v) for v in value]
        elif hasattr(value, "__dict__"):
            return self.__convert_dict(value.__dict__)
        else:
            return value


class Student(MapMixin, DictMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.__dict__)


if __name__ == "__main__":
    s = Student("Jack", 20)
    print(s["name"])
    print(Student.__dict__)
    print(s.__dict__)
    print(s.to_dict())
