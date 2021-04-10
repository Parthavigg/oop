class rect:
    def __init__(self,length,breadth):
        print("I'm initialising the rectangle class")
        self.length=length
        self.breadth=breadth
    def area(self):
        self.area=self.length*self.breadth
        print("Area is",self.area)
    def __del__(self):
        print("Instance destroyed")
c=rect(20,30)
c.area()
cl=rect(20,40)
cl.area()
cl.__del__()
