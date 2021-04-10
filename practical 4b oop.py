class Employee:
    def __init__(self):
        self.comp_name=str(input("Enter company name:"))
        self.comp_add=str(input("Enter your company address:"))
        self.emp_id=int(input("Enter your emp id:"))
        self.name=str(input("Enter your name:"))
        self.qual=str(input("Enter your qualification:"))
        self.des=str(input("Enter your designation:"))
        self.basic_sal=int(input("Enter your basic salary:"))
        
    def calc(self):
         TA=18/100*self.basic_sal
         DA=70/100*self.basic_sal
         HRA=25/100*self.basic_sal
         EPF=10/100*self.basic_sal
         net_sal=self.basic_sal+TA+DA+HRA+EPF
         print("Net salary is:",net_sal)
    def __del__(self):
          print("Instance destroyed")

c=Employee()
c.calc()
c.__del__()
