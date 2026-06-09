
class animal:              # THIS IS PARENT CLASS
    a = 12
    def __init__(self,name):
        self.name =  name  

    def details(self):
        print(f"my name is {self.name}")
    

class human(animal):   # THIS IS CHILD CLASS
    pass


obj = animal("lion")

obj2 = human("rahul")

obj2.details()

print(obj.a)
    
# YOUR CHILD CLASS OBJECT HASS ALL POWER TO ACESS 
# THE ATTRIBUTES AND METHODS OF PARENT CLASS


# CONSTRUCTOR INHERITANCES
# MULTILEVEL INHERITANCES
class bagFactory:
    def __init__(self, material, zips, pocket):
        self.material = material
        self.zips = zips
        self.pocket = pocket

    def details(self):
        print("Your bag details are:")
        print("Material :", self.material)
        print("Zips :", self.zips)
        print("Pockets :", self.pocket)

# SINGLE LEVEL INHERITANCES
class reebok(bagFactory):
    def __init__(self, material, zips, pocket, color):
        super().__init__(material, zips, pocket)        # SUPER CALL PARENTS CLASS
        self.color = color

    def details(self):
        print("Color :", self.color)
        super().details()

# MULTILEVEL INHERITANCES
class campus(bagFactory):
    def __init__(self, material, zips, pocket):
        super().__init__(material, zips, pocket)
    

bag1 = bagFactory("leather", 3, 4)

bag2 = reebok("polyster", 4, 2, "red")

bag1.details()
bag2.details()




# MULTIPLE INHERITANCES

# MULTIPLE INHERITANCE

class animal:
    def __init__(self, name):
        self.name = name

class humans:
    def __init__(self, Id):
        self.Id = Id

class Robots(animal, humans):
    def __init__(self, namen, Id):
        animal.__init__(self, namen)
        humans.__init__(self, Id)

    def details(self):
        print("Name :", self.name)
        print("ID :", self.Id)

robo = Robots("rahul", 12)
robo.details()



