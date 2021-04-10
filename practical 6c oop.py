#Program to demonstrate Multiple Inheritance


class Base1(object):

    def __init__(self):
        self.str1 = "Hello"
        print(self.str1)
        print("komal")


class Base2(object):

    def __init__(self):
        self.str2 = "Hi"
        print(self.str1)
        print("Devangi")


class Derived(Base1 , Base2):

    def __init__(self):
        Base1. __init__(self)
        Base2. __init__(self)
        print("Nice TO meet you")

    def displayStr(self):
        print(self.str1, self.str2)


c = Derived()
c.displayStr()

