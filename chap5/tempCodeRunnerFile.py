# que 1 =  ACCEPT TWO NUMBER AND PRINT THE GRETEST BETWEEN THEM

num1 = int (input("PLEASE GIVE ME FIRSST NUMBER :- "))
num2 = int (input("PLEASE GIVE ME SECOND NUMBER :- "))

if num1 > num2:
    print(f"{num1} IS GREATER THAN {num2}")

elif num2 > num1:
     print(f"{num2} IS GREATER THAN {num1}")

else:
    print("BOTH THE NUMBERS ARE EQUAL")

