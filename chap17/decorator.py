
# @

def extragreeting(func):
    def wrapper():
        print("hello rahul")
        func()
        print("thanku visit again")

    return wrapper




@extragreeting       #  THIS IS GREETING METHODS
def greeting():
    print('good morning')


greeting()