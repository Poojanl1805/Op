txt = "Hello World!!!"
x = txt.capitalize()
print(x)

txt = "Hello World!!!"
print(txt.capitalize())

txt = "Hello World!!!"
print(txt.casefold())

txt = "Hello World!!!"
print(txt.center(30))

txt = "Hello  world Hello World!!!"
print(txt.count("Hello",5,7))


txt = "Hello guys"
print(txt.endswith("guys"))

txt = "H\te\tl\tl\to\tg"
print(txt.expandtabs(3))

txt = "H\te\tl\tl\to"
print(txt.expandtabs(4))

txt="My name is Pooja.N.L"
y=txt.encode()
print(y)

txt = "Hello guys"
print(txt.format())


txt = "Hello guys"
print(txt[1:5])

a="hello"
b="world"
c= a +" "+ b
print(c)


name="pooja"
age="twenty-two"
txt="My name is {} , My age is {}"
print(txt.format(name,age))

name="pooja"
age=21
txt="My name is {} , My age is {}"
print(txt.format(name,age))

txt="we are   called \'champians\' due to our history"
print(txt)

print(10<9)
print(10>=6)
print(10==10)

a=837
b=9210
if a<b:
    print(a," is smaller")
else:
    print(a," is bigger")

print(bool(None))
print(bool(1))
print(bool(['apple','banana']))

def myfunc():
      return True
if myfunc():
    print("yes")
else:
    print("no")
    
x=str(499)
print(isinstance(x,str))


x=["car","bike","truck"]
y=["car","bike","truck"]
z=y
print(x is  y)
print(y is  x)
print(y is  z)

list1=["Suntv","VijayTv","RajTv","JayaTv"]
list2=["Sunews","Polimmer","Jayanews"]
list1.extend(list2)
print(list1)

a=["apple","orange","grape","cherry"]
a.remove("orange")
print(a)


a=["apple","orange","grape","cherry"]
a.pop(2)
print(a)


thislist=["apple","orange","grape","cherry"]
del thislist
print(thislist)


thislist=["apple","orange","grape","cherry"]
thislist.clear()
print(thislist)

my_list=["apple","orange","mango","fig"]
for i in range(len(my_list)):
    print(my_list[i])
    
my_list=["apple","orange","mango","fig"]
i=0
while i<len(my_list):
    print(my_list[i])
    i=i+1
    
my_list=["apple","orange","mango","fig"]#list comprehension-for short syntax
[print(x)for x in my_list]


my_list=["apple","orange","mango","fig"]#list comprehension-for short syntax
newlist=[]
for x in my_list:
    if "a" in x:
        newlist.append(x)
print(newlist)

x=bytearray(5)#used in banking sectos,intel processor(where memory allocation used)
print(x)