class shape:
    def  _get_Length_Breadth(self):
        self._length = int(input("Enter Length : "))
        self._breadth = int(input("Enter breadth :"))

class Rectangle(shape):
    def calculate_area(self):
        print("Area of rectangle is",self._length*self._breadth)

obj =Rectangle()
obj._get_Length_Breadth()
obj.calculate_area()
