

# QUE 1 = PRINT "HELLO WORD" N TIMES

n = int(input("TELL YOUR NAME := "))

for i in range(n):
    print("hello word")

# QUE 3 = REVERSE FOR LOOP - PRINT N DOWN TO 1

n = int(input("PLEASE TELL YOUR NUMBER :- "))
for i in range(n,0,-1):     # REVERSE SATHI -1 MADHI GHAYCH KARAN MAGE MAGE YET AHE VALUES
    print(i)





# QUE 4 = PRINT THE MULTIPLICATION TABLE OF A NUMBER

n = int(input("PLEASE TELL YOUR table :- "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")






# QUE 9 = CHECK IF NUMBER IS PERFECT (SUM OF FACTOR =  THE SUM OF ITSELF)

n = int(input("PLEASE TELL YOUR NUMBER :-"))

s = 0

for i in range(1,n):
    if n % i ==0:
        s = s + i

if s ==n:
    print("PERFECT NUMBER")

else:
    print("NOT A PERFECT")





# QUE 11 = REVERSE A STRING WITHOUT USING BUILT IN FUCTION

a = "python"

rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

print(rev)



# QUE 13 = COUNT LETTERS,DIGITS,AND SPEICAL SYMBOL IN A STRING 

a = "1jnik2819n$%^bj"

char = 0
spchar = 0
digits = 0

for i in a:
    if i.isdigit():
        digits = digits + 1
    elif i.isalpha():
        char = char + 1
    else:
        spchar = spchar + 1

print(f"character {char} , speical character {spchar} , digits {digits}")