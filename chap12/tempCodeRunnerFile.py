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