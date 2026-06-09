
def addition(*args):
    s = 0
    for i in args:
        s = s + i
  

print(addition(10,20,33,44,5,5,5,60))



# DICTINORY
def info(**kwargs):
    return kwargs

print(info(name = "rahul" , age = 21 , surname = "gunjal"))









# @

def extragreeting(func):
    def wrapper(*args,**kwargs):
        print("hello rahul")
        func(*args,**kwargs)
        print("thanku visit again")

    return wrapper




@extragreeting       #  THIS IS GREETING METHODS
def addition(a,b,c,):
    print(a+b+c)


addition(10,20,30)