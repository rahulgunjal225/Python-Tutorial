
# Polymorphism means "many forms". 
# It allows the same method, function, or operator to behave differently depending on the object or data it is used with.



class animal:
    def speak(self):
        print("animal will not speak")

class human:
    def speak(self):
        print("we are human we can speak")

obj = animal()
obj2 = human()

obj.speak()
obj2.speak()     # SAME NAME BUT GIVES DIFFERENT RESPONSE

# TYPES
# 1. METHOD OVERRIDING
# 2. METHOD OVERLOADING

