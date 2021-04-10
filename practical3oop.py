class Book:
    def accept(self):
        self.name=str(input("Enter name of the Book: "))
        self.author=str(input("Enter author of the Book: "))
        self.price=float(input("Enter price of the Book: "))
        self.n_copies=int(input("Enter number of copies: "))
    def total_price(self):
        t=self.price*self.n_copies
        print("Total Price: ",t)
    def details(self):
        print("Purchase details".center (70,"-"))
        print("Name of book:",self.name)
        print("Author of book:",self.author)
        print("Price of book:",self.price)
        print("Number of copies:",self.n_copies)

c= Book()
c.accept()
c.details()
c.total_price()
        
