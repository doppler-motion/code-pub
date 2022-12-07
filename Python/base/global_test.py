a = 0


def func1():
    global a
    print(a)
    for i in range(10):
        print(i)


def func2():
    global a

    func1()
    a = 10
    print("a", a)


func2()