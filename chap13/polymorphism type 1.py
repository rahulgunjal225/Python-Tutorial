
#1.  METHOD OVERRIDING ( WE NEED INHERITANCES)
# WHEN INHERITANCES USED KARTO PARENT METHOD AND CHILD METHOD 
# 2 CH PN NAME SAME ZALL TRR TYALA OVERRIDING MHANATAT

class Animal:
    a = 12
    def __init__(self,name):
        self.name = name

    def details(self):
        print(f"your name is {self.name}")

class Humans(Animal):
    b = 11
    def details(self):
        super().details()      # HE LIHL MHANUN 2 PN TARGET ZALEE
        print(f"your info is {self.name} and this is all we have ")

obj = Humans("rahul")
# HUMANS MADHLA DETAILS METHOD TARGET HOT 

obj.details()    # DETAILS METHOD ARE SAME

# JRR 2 PNN TARGET KARYCH ASEL TR SUPER().DETAILS()  USED KARNE    

# WHEN WE ARE DOING INHERITANCES AND PARENT AND CHILD CLASSES HAVE SAME METHOD NAME
# SO THE CHILD CLASS METHOD WILL OVERIDE YOUR PARENT CLASS METHOD
        