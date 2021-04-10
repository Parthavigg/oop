import math

class Polygons:
    def number_of_sides(self):
        return 0
    def area(self):
        return 0
    def perimeter(self):
        return 0


class Triangle(Polygons):
    def number_of_sides(self):
        return 3
    def area(self):
        base=10
        height=12
        return 1 / 2 * base * height

    def perimeter(self):
        a=10
        b=10
        c=12
        if a + b > c:
            return a+b+c
        else:
            return"Invalid input make sure a+b>c"

class Rhombus(Polygons):
    def number_of_sides(self):
        return 4
    def area(self):
        p=4
        q=5
        return p*q/2
    def perimeter(self):
        a=5
        return 4*a

tri = Triangle()
print("Triangle Area:",tri.area())
print("perimeter:",tri.perimeter())
print("--------------------------")


rho = Rhombus()
print("Rhombus Area:",rho.area())
print("perimeter:",rho.perimeter())
print("--------------------------")

      
    

    
    
