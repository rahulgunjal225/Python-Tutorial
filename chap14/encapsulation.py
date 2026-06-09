
# Encapsulation is the process of wrapping data (variables) and methods (functions) into a single unit called a class and restricting direct access to some data.

# It helps in data hiding and protects the object's data from unauthorized access.

# PUBLIC
class Factory:
    name = "kia"      # PUBLIC CLASS ATTRIBUTES
    # _old = 12         # PROTECTED  [used  _  ] does not used exist
    def __init__(self, type , tyre , color):
        self.color = color   # PUBLIC OBJECT ATTRIBUTES
        self.tyre = tyre
        self.type = type

    def detail(Self):     # PUBLIC METHOD
        print("hello your detials are : ")
        

obj = Factory("sedan" , "MRF" , "WHITE")

obj.name = "MARUTI"
print(obj.name)

# obj.detail()



# PRIVATE    [USED __   ]

class Factory:
    __name = "kia"      # PRIVATE CLASS ATTRIBUTES  {USED __ {DOUBLE UNDERSCORE}}
    a = 12              # PUBLIC CLASS ATTRIBUTES
    # _old = 12         # PROTECTED  [used  _  ] does not used exist
    def __init__(self, type , tyre , color):
        self.__color = color   # PRIVATE OBJECT ATTRIBUTES
        self.tyre = tyre
        self.type = type

    def __detail(Self):     # PUBLIC METHOD
        print("hello your detials are : ")
        
class hello(Factory):
    print(Factory.a)
    print(Factory.__name)

obj = Factory("sedan" , "MRF" , "WHITE")

# obj.name = "MARUTI"
print(obj.__name)
obj.__detail()



# USE METHOD [DOES NOT USED ]

class hello:
    __a = 12

    @classmethod
    def info(cls):
        print(cls.__a)

obj = hello()
obj.info()