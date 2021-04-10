class Circle:
    def CalculateArea(self):
        print("Enter radius:")
        self.r=float(input())
        area=3.14*self.r*self.r
        print("Area of Circle is =%f"%(area))


    def CalculatePerimeter(self):
        perimeter=2*3.14*self.r
        print("Perimeter of Circle is =%f"%(perimeter))
        



c=Circle()
c.CalculateArea()
c.CalculatePerimeter()
