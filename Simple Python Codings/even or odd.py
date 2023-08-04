a=int(input("Enter a num:"))
flag=a%2
if flag==0:
    print("num is even")
else:
    print("num is odd")


start=int(input("Enter the start value:"))
end=int(input("Enter the end value:"))
a=[]
for i in range(start,end):
    if (i%2!=0):
      a.append(i)
print("The odd numbers from",start, "and" ,end,"are",a)
      
