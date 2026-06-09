
class bags:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    

reebok = bags("leather" , 3 , 2)
campus = bags("polyster" , 2 , 5)

print(reebok.material)
print(campus.material)