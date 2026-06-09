
# que 1 =  ACCEPT TWO NUMBER AND PRINT THE GRETEST BETWEEN THEM

num1 = int (input("PLEASE GIVE ME FIRSST NUMBER :- "))
num2 = int (input("PLEASE GIVE ME SECOND NUMBER :- "))

if num1 > num2:
    print(f"{num1} IS GREATER THAN {num2}")

elif num2 > num1:
     print(f"{num2} IS GREATER THAN {num1}")

else:
    print("BOTH THE NUMBERS ARE EQUAL")



# que 2 = ACCEPT GENDER FROM USER AND PRINT A GREETING MESSAGE

print("Hello" > "hello") # string chya atmdhe conditon operator are used

gen = input("PLEASE TELL YOUR GENDER IN (M OR F) :- ")

if gen == "M" or gen == "m":
    print("HELLO SIR")

elif gen == "F" or gen == "f":
    print("HELLO MAM")

else:
    print("OTHERS")


# que 3 = ACCEPT AN INTEGER AND CHECK IF IT IS EVEN OR ODD
# even = ( 2,4 ,6 ,8 ...)
# odd = ( 1,3,5,,7......)

a = int(input(" PLEASE TELL YOUR NUMBER :- "))

if a % 2 ==0:
    print("EVEN NUMBER")

else:
    print("ODD NUMBER")



# que 4 = ACCEPT NAME AND AGE - CHECK IF THE USER IS A VALID VOTER (18+)

name = input("PLEASE TELL YOUR NAME :- ")

age = int(input("PLEASE TELL YOUR AGE :- "))

if age >= 18:
    print(f"HELLO {name} YOU ARE A VALID VOTER")

else:
    print(f"HELLO {name} YOU CAN VOTE AFTER {18 - age} YEARS")



# que 5 = ACCEPT A YEAR AND CHECK IF IT IS A LEAP YEAR
# 1900 yaers la % 400 and 2000(century years) years la %4

year = int(input("PLEASE TELL YOUR YEAR :- "))

if year %100 ==0 and year %400==0:
    print("LEAP YEAR")

elif year %100 != 0 and year %4 ==0:
    print("LEAP YEARS ")

else:
    print("NOT A LEAP YEARS")


# que 6 = ACCEPT TEMPRETURE IN 0C AND PRINT A DESCRIPTION

temp = int(input("PLEASE TELL YOUR TEMPRATURE :- "))

if temp >= -5 and temp <= 5:
    print("VERY COLD")

elif temp >=6 and temp <= 18:
    print("COLD")

elif temp >= 19 and temp <= 30:
    print("HOT")

else:
    print('VERRY HOT')
