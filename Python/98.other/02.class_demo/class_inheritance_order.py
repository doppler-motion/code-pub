class Base(object):
    def __init__(self):
        print("base created.")
        

class childA(Base):
    def __init__(self):
        print("child A")
        super(childA, self).__init__()
        

class childB(Base):
    def __init__(self):
        print("child B")
        super(childB, self).__init__()


class childC(Base):
    def __init__(self):
        print("child C")
        super(childC, self).__init__()


class childD(childA, childB):
    def __init__(self):
        print("child D")
        super(childD, self).__init__()


class childE(childB, childC):
    def __init__(self):
        print("child E")
        super(childE, self).__init__()


class childF(childD, childE):
    def __init__(self):
        print("child F")
        super(childF, self).__init__()


F = childF()

print(childF.mro())
