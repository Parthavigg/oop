#Program demonstrating the concept corpostion

#Creating container class

class Salary:

    def __init__(self,pay):
        self.pay = pay

    def get_total(self):
        return (self.pay*12)

class Employee:

    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus


    def annual_sal(self):
        return 'Total:'+str(self.pay.get_total()+self.bonus)


#Creating objects
obj_sal = Salary(70000)
obj_exp = Employee(obj_sal,30000)
print(obj_exp.annual_sal())
    
