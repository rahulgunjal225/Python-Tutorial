
class animal:
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return f"hello my name is {self.name}"
    

obj = animal("lion")
obj1 = animal("tiger")
print(obj)
print(obj1)


class number:
    def __init__(self,num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num
    
    def __eq__(self, value):
        return self.num == value.num

num1 = number(40)
num2 = number(40)

print(num1 + num2)
print(num1 == num2)