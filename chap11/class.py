
class car:
    a =12    # ATTRIBUTES

    def hello(): # METHODS
        print("how are you")

# YOU CAN ACESS ATTRIBUTES AND METHODS AFTER ACESSING THE CLASS

print(car.a)   # ACCESSING ATTRIBUTES
car.hello()    # ACCESSING METHODS



#  OBJECT

class bags:
    name = "RAHUL GUNJAL"

    def details(self):
        print("hello this is a company who creates bag")

object = bags()    # [AGOTHER OBJECT NAVACH VARIBALE BANVL NTR TYACHYAT OBJECT DEFINES KEL] THIS IS CREATE OBJECT
campus = bags()
print(object.name)
print(campus.name)

object.details()