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