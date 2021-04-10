Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Add:
    a=1
    b=2
    def __init__(self):
        self.a=5
        self.b=10
    def calculate(self):
        print("a=",self.a)
        print("b=",self.b)
        init_sum=(self.a+self.b)
        print("sum is",init_sum)
        print("a=",Add.a)
        print("b=",Add.b)
        class_sum=Add.a+Add.b
        print("sum is",class_sum)
        al=Add()
        al.calculate()
                