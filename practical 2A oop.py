class bank:
    cust_name=str(input("Enter your name:"))
    acc_no=int(input("Enter your account number:"))
    bal=int(input("Enter your balance:"))

    def deposit(self):
        dep_amt=int(input("Enter the amount to be deposit:"))
        self.bal=self.bal+dep_amt
        print("Current balance is",self.bal)
        
    def withdraw(self):
       with_amt=int(input("Enter the amount to be withdraw:"))
       self.bal=self.bal-with_amt
       print("Your current balance is",self.bal)
c=bank()
a=int(input("Enter 1 is you want to deposit some  amount or 2 if you want to withdraw:"))
if(a==1):
   c.deposit()
elif(a==2):
    c.withdraw()
        
