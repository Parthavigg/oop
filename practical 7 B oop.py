#method overloading
class employee:
    def add(self, salary,incentive):
        print('Total salary in base class=' , salary+incentive)



class department(employee):
    temp = '1 m member of dept class'

    def add(self, salary , incentive):
        print(self.temp)
        print('Total salary in derived class=', salary+incentive)

dept = department()
dept.add(45000,5000)
