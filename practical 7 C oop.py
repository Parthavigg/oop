#method overloading using(super)
class Employee:
    def add(self, salary,incentive):
        print('Total salary in base class=' , salary+incentive)



class Department(Employee):
    temp = '1 m member of dept class'

    def add(self, salary , incentive):
        print(self.temp)
        print('Total salary in derived class=', salary+incentive)
        super(Department,self).add(salary,incentive)

dept = Department()
dept.add(45000,5000)
