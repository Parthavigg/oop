class student:

    def acceptData(self):
        self.rollno = int(input("Roll No : "))
        self.name = str(input("Name  : "))
        self.class_ = str(input("class  : "))
        self.div = str(input("Division  : "))
        self.sem = input("semester : ")

class Marks(student):

    def accept_marks(self):
        self.dm = int(input("Discrete Mathematics : "))
        self.pp = int(input("Python Programming    : "))
        self.oops = int(input("object oriented programming  : "))
        self.dbms = int(input("Database management system : "))
        self.wp = int(input("web programming  : "))
        self.it = int(input("IT tools : "))

class Result(Marks):

    def calculate(self):
        self.total = (self.dm+self.pp+self.oops+self.dbms+self.wp+self.it)
        self.avg = self.total/6
        self.percentage = (self.total * 100)/600
        print("\nTotal Marks : ",self.total)
        print("Average Marks : ",self.avg)
        print("Percentage : ",self.percentage)

c=Result()
c.acceptData()
c.accept_marks()
c.calculate()
