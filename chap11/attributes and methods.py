
# TYPES OF ATRRIBUTES

class animal:
    a = 12      # CLASS ATTRIBUTES

    def __init__(self,name):
        self.name = name    # OBJECT / INSTANCES ATTRIBUTES
         

    def hello(self):     #  INSTANCES / OBJECT METHODS CAPTURE THE LOCATION OF OBJ
        print(f"how are you my name is {self.name}")


    @classmethod  # DECORATOR
    def details(cls):      # CLASS METHOD  CAPTURE THE LOCATIN OF CLASS
        print(f"how are you my name is {cls.a}")

    @staticmethod
    def speak():       # STATIC METHOD AND IT WILL NOT TARGET ANY LOCATION
        print("how are you i am a static method")



obj = animal("lion")


obj.hello()
obj.details()
