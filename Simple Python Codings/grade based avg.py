a=int(input("Enter your Tamil Mark:"))
b=int(input("Enter your English Mark:"))
c=int(input("Enter your Maths Mark:"))
avg=(a+b+c)/3
print("Your average is",avg)
if(avg>=90):
    print("you are O grade")
elif(avg>=80 and avg<=90):
    print("you are A+ grade")
elif(avg>=70 and avg<=80):
    print("you are A grade")
elif(avg>=60 and avg<=70):
    print("you are B grade")
else:
    print("You are failed")