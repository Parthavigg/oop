# Python program showing use of property() function.
class property_fun_demo:
    # def __init__(self):
    # self. __age = 0
    
    # function to get values of _age.
    def get_age(self):
        print("Getter method called. ")
        return self._age

    #function to set values of _age.
    def set_age(self,a):
        print("Setter method called. ")
        self._age = a

    # function to delete _age attribute.
    def del_age(self):
        print("Object deleted")
        del self._age
        
    age = property(get_age,set_age,del_age)

mark = property_fun_demo()
mark.age = 10
print(mark.age)
mark.del_age()
    
