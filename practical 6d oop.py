class Details:
    
    def _init_(self):
        self.__id ="<No Id>"
        self.__name ="<No Name>"
        self.__gender="<No Gender>"

    def setData(self, id, name,gender):
         self.__id = id
         self.__name = name
         self.__gender= gender

    def showData(self):
        print("Id : ",self.__id)
        print("Name : ",self.__name)
        print("Gender : ",self.__gender)

class Employee(Details):

    def __init__(self):
        self.__company ="<No Company>"
        self.__dept ="<No Dept>"

    def setEmployee(self, id, name, gender, comp, dept):
        self.setData(id , name,gender)
        self.__company = comp
        self.__dept = dept

    def showEmployee(self):
        self.showData()
        print("Company : ",self.__company)
        print("Department : ",self.__dept)

class Doctor(Details):

    def __init__(self):
        self.__hospital ="<No Hospital>"
        self.__dept = "<No Dept>"

    def setEmployee(self, id, name, gender, hos, dept):
        self.setData(id, name, gender)
        self._hospital = hos
        self.__dept = dept

    def showEmployee(self):
        self.showData()
        print("Hospital : ",self.__hospital)
        print("Department : ",self.__dept)

def main():
     print("Employee Object")
     e = Employee()
     e.setEmployee(1, "Komal Menaria", "Female", "gmr", "excavation")
     e.showEmployee()
     print("\nDoctor object")
     d = Doctor()
     d.setEmployee(1, "Devangi Parmar", "Female", "aiims", "eyes")
     d.showEmployee()
 
if __name__ == "__main__":
        main()
