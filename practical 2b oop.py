class marks:
    student_name=str(input("Enter your name:"))
    student_rno=int(input("Enter your roll no:"))
    sclass=input("Enter your class:")

    def subjects(self):
        self.dbms=int(input("Enter marks in DBMS:"))
        self.dm=int(input("Enter marks in DM:"))
        self.pp=int(input("Enter marks in python programming:"))
        self.oop=int(input("Enter marks in object oriented programming:"))
        self.wp=int(input("Enter marks in web programming:"))

    def internal_marks(self):
        print("Enter your marks out of 40 for internals:")
        self.subjects()
        self.int_marks=self.dbms+self.dm+self.pp+self.oop+self.wp

    def theory_marks(self):
        print("Enter your marks out of 60 for theory:")
        self.subjects()
        self.th_marks=self.dbms+self.dm+self.pp+self.oop+self.wp

    def practicals(self):
        print("Enter your marks out of 50 for practicals:")
        self.subjects()
        self.pr_marks=self.dbms+self.dm+self.pp+self.oop+self.wp
        self.marks=self.int_marks+self.th_marks+self.pr_marks
        self.total=(40*5)+(60*5)+(50*5)
        self.percent=(self.marks/self.total)*100
        self.percentage=round(self.percent)

    def grade(self):
      if self.percentage>90:
         print("You pass!")
         print("Your percentage is:",self.percentage)
         print("O Grade")
      elif self.percentage>75:
         print("You pass!")
         print("Your percentage is:",self.percentage)
         print("A+ Grade")
      elif self.percentage>60:
         print("You pass!")
         print("Your percentage is:",self.percentage)
         print("A Grade")
      elif self.percentage>50:
         print("You pass!")
         print("Your percentage is:",self.percentage)
         print("B+ Grade")
      elif self.percentage>45:
         print("You pass!")
         print("Your percentage is:",self.percentage)
         print("B Grade")
      else:
         print("You Fail!")
         print("Your percentage is:",self.percentage)

    def display(self):
         print("Your name is:",self.student_name)
         print("Your roll no is:",self.student_rno)
         print("Your class is:",self.sclass)
         print("Your total marks:",self.total)
         print("Your percentage:",self.percentage)

c=marks()
c.internal_marks()
c.theory_marks()
c.practicals()
c.display()
c.grade()
         
             
             
                   
    
