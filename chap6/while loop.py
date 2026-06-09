
# infinite paryant chalt

#a = 1
#while True:
 #   print(a)
  #  a = a + 1

a = 1
while a != 20:
    print(a)
    a = a + 1



# QUE 1 = SEPRATE EACH DIGIT NUMBER AND PRINT ON A NEW LINE

a = int(input("PLEASE TELL YOUR NAME :- "))

while a > 0:
    print(a % 10)

    a = a // 10


# QUE 2 = ACCEPT A NUMBER AND PRINT ITS REVERSE

a = int(input("PLEASE TELL YOUR NAME :- "))

rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

print(rev)


# QUE 3 = CHECH IF A NUMBER IS PALINDROMIC (EQUAL TO ITS REVERSE)

a = int(input("PLEASE TELL YOUR NAME :- "))

copy = a

rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

if rev == copy:
    print("IT IS A PALINDROME")

else:
    print("NOT PALINDROME")


