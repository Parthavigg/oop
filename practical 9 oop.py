from abc import ABC
import math


class Shape(ABC):

    def no_of_sides(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def no_of_sides(self):
        self.length = int(input("Enter length : "))
        self.breadth = int(input("Enter Breadth : "))

    def calculate_area(self):
        print("Area of Rectangle : ",self.length*self.breadth,"\n")

    def calculate_perimeter(self):
        print("Perimeter of rectangle : ",2*(self.length+self.breadth),"\n")

class Square(Shape):

    def no_of_sides(self):
        self.side = int(input("Enter side : "))

    def calculate_area(self):
        print("Area of square : ",self.side**2,"\n")

    def calculate_perimeter(self):
        print("Perimeter of square : ", 4 * self.side,"\n")

class Circle(Shape):

    def no_of_sides(self):
        self.radius = int(input("Radius : "))

    def calculate_area(self):
        print("Area of circle : ", (22/7)*self.radius*2)

    def calculate_perimeter(self):
        print("Perimeter of circle : ", 2*(22/7)*self.radius,"\n")

class Ellipse(Shape):

    def no_of_sides(self):
        self.semiMajorAxis = int(input("Enter Semimajor Axis : "))
        self.semiMinorAxis = int(input("Enter Semiminor Axis : "))

    def calculate_area(self):
        print("Area of Ellipse : ",(22/7) * self.semiMajorAxis * self.semiMinorAxis)

    def calculate_perimeter(self):
        print("Perimeter of Ellipse : ",2 * (22/7) ** math.sqrt((self.semiMajorAxis + self.semiMinorAxis)/2))


obj = Rectangle()
obj.no_of_sides()
obj.calculate_area()
obj.calculate_perimeter()

obj1 = Square()
obj1.no_of_sides()
obj1.calculate_area()
obj1.calculate_perimeter()

obj2 = Circle()
obj2.no_of_sides()
obj2.calculate_area()
obj2.calculate_perimeter()

obj3 = Ellipse()
obj3.no_of_sides()
obj3.calculate_area()
obj3.calculate_perimeter()
