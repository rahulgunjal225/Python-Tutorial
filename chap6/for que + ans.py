
# QUE 2 = PRINT NATURAL NUMBER FROM 1 TO N

n = int(input("PLEASE TELL YOUR NUMBER :- "))

for i in range(1,n+1):     # [n+1 mhanje userr jo number denar tit paryant aal pahije{jrr n ghetl ast trr 1step mage stop zal ast}]
     print(i)
        

# QUE 5 = SUM OF FIRST N NATURAL NUMBER

s = 0
n = int(input("PLEASE TELL YOUR NAME :- "))

for i in range(1,n+1):
     s = s + i

print(s)


# QUE 6 = FACTORIAL OF NUMBER

f = 1
n = int(input("PLEASE TELL YOUR NAME :- "))

for i in range(1,n+1):
     f = f * i

print(f)


# QUE 7 = PRINT SUM OF ALL EVEN AND ODD NUMBER IN RANGE SEPREATLY

n = int(input("PLEASE TELL YOUR NAME :- "))

oddsum = 0
evensum = 0

for i in range(1,n+1):
     if i %2 == 0:
          evensum = evensum + i
     else:
      oddsum = oddsum + i

print(f"YOUR EVEN SUM IS {evensum} AND ODD SUM IS {oddsum}")


    

# QUE 8 = PRINT ALL FACTORS OF A NUMBER 

# facors mhanje jya number na divide karel
# jyache 2 factors asel to prime 
# jyache 2 peksha jast asel to composite

n = int(input("PLEASE TELL YOUR NAME :- "))

for i in range(1,n+1):
    if n % i == 0:
        print(i)



# QUE 10 = CHECK IF A NUMBER IS PRIME 

n = int(input("TELL YOUR NAME :-"))

count = 0

for i in range(1,n+1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("PRIME NUMBER")

else:
    print("COMPOSITE NUMBER")



# QUE 12 = CHECK IF A STRING IS A PALINDROME



a = input("TELL YOUR STRING :- ")

rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

if rev ==a:
    print("YES PALIDROME")

else:
    print("NOT A PALINDROME")

