class Rectangle:
    def CalculateArea(self):
        print("Enter length:")
        self.l=float(input())
        print("Enter breadth:")
        self.b=float(input())
        area=self.l*self.b
        print("Area of rectangle is =%f"%(area))


    def CalculatePerimeter(self):
        perimeter=2*(self.l+self.b)
        print("Perimeter of rectangle is =%f"%(perimeter))
        



c=Rectangle()
x=c.CalculateArea()
y=c.CalculatePerimeter()
