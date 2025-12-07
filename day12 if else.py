a=int(input("enter your age "))
print("your age is :",a)
#conditional operators
#<,>,<==,>==,==,<=,!=
#print(a<18)
#print(a<18)
#print(a<=18)
#print(a>=18)
#print(a==18)
#print(a!=18)

if(a>18):
    print("you can drive")
else:
    print("you cannot drive")


mangoprice=210
budget=200
if(mangoprice <= budget):
    print("ashu,add 1kg mango to the cart")
else:
    print("ashu,do not add mango to the cart")


num=int(input("enter the value of num:"))
if(num<0):
    print("number is negative")
elif(num==0):
    print("numbe is zero")
else:
    print("number is positive")