n=int(input("Enter how many num you need to fin avg:"))
a=[]
for i in range(0,n):
  element=int(input("Enter your value:"))
  a.append(element)
avg=sum(a)/n
print("avg val is",avg)