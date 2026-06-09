
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
    ("NOT PALINDROME")


