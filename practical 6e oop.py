class Parent:

    def func1(self):
        print("this is function one")

class child(Parent):

    def func2(self):
        print("this is function 2")

class child1(Parent):

    def func3(self):
        print("this is function 3")

class child3(child , child1):

    def func4(self):
        print("this is function 4")

ob = child3()
ob.func1()
ob.func2()
ob.func3()
ob.func4()
