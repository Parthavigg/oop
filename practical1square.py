class Square:
    def CalculateArea(self):
        print("Enter side:")
        self.s=float(input())
        area=self.s*self.s
        print("Area of Square is =%f"%(area))


    def CalculatePerimeter(self):
        perimeter=4*self.s
        print("Perimeter of Square is =%f"%(perimeter))
        



c=Square()
c.CalculateArea()
c.CalculatePerimeter()
