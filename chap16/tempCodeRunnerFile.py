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