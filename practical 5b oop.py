# to demonstrate the use of getter and setter method using property decorator.
class property_decorater_demo:
    def __init__(self):
        self._age = 0


    @property
    def get_age(self):
         print("Getter method called. ")
         return self._age

    @get_age.setter
    def age(self,a):
         if(a < 18):
             raise ValueError("Sorry your age is below eligibility criteria.")
         print("Setter method called.")
         self._age =a

# Creating a object of class.
mark = property_decorater_demo()

#Calling method through object.
mark.age = 19
print(mark.age)
