x,y=5,3

print("x =",x,"y=",y)

print("\nx + y=",x+y)
print("x.__add__(y)=",x.__add__(y))

print("\nx * y=",x*y)
print("x.__mul__(y)=",x.__mul__(y))

print("\nx / y=",x/y)
print("x.__truediv__(y)=",x.__truediv__(y))

print("\nx ** y=",x**y)
print("x.__pow__(y)=",x.__pow__(y))

print("\nx % y=",x%y)
print("x.__mod__(y)=",x.__mod__(y))

print("\nx == y=",x==y)
print("x.__eq__(y)=",x.__eq__(y))

print("\nx != y=",x!=y)
print("x.__ne__(y)=",x.__ne__(y))

print("\nx >= y=",x>=y)
print("x.__ge__(y)=",x.__ge__(y))

print("\nx <= y=",x<=y)
print("x.__le__(y)=",x.__le__(y))
print("------------------------------")

str1 = "special method"
print("\nstr1=",str1)

print("\n'ods' in str1=","ods"in str1)
print("str1.__contains__('ods')=",str1.__contains__("ods"))

print("\n len(str1) =",len(str1))
print("str1.__len__() =",str1.__len__())

list1=[5,3,20]
print("\nlist1 =",list1)

print("\nlist[1] =",list1[1])
print("list1.__getitem__(1)=",list1.__getitem__(1))

print("str(list1)=",str(list1))
