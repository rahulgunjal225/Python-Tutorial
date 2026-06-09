
# IMMUTABLE [ CANNOT CHANGES ANY VALUES INSIDE YOUR TUPLES]
# USED PARANTHESIS ()

a = ()

print(type(a))
#      0 ,      1 ,  2   {index}
b = ("MONDAY", 123,"TUESDAY", 111,11,111,1,1,1,1,1)

tup = tuple(b)

print(type(tup))
print(tup[0])

# METHODSS
# INDEX
# COUNT


print(tup.index("MONDAY"))
print(tup.count(1))



def student():
    return "rahul",21,"rahul@gmail.com"

info = student()

print(info)

name, age , email = info

print(name)