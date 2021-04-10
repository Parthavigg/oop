import math
class Ellipse:
    def CalculateArea(self):
        print("Enter axis 1:")
        self.a=float(input())
        print("Enter axis 2:")
        self.b=float(input())
        area=3.14*self.a*self.b
        print("Area of ellipse is =%f"%(area))


    def CalculatePerimeter(self):
        perimeter=2*3.14*math.sqrt((self.a*self.a+self.b*self.b)/(2))
        print("Perimeter of ellipse is =%f"%(perimeter))
        



c=Ellipse()
x=c.CalculateArea()
y=c.CalculatePerimeter()
