
# function
#print()
#float()
#input()
#int()
#len()

def hello():        # THIS IS REUSABLE FUNCTION
    print("hello,how are you")
    print("wellcome")

hello()   # CALL KARYLA LAGT TEVHA FUNCTION RUN HONAR [JEVDHYA VELA CLL KARNAR TEVDHYA VELES RUN HONAR]
hello()   # CALL KARYLA LAGT TEVHA FUNCTION RUN HONAR [JEVDHYA VELA CLL KARNAR TEVDHYA VELES RUN HONAR]
hello()   # CALL KARYLA LAGT TEVHA FUNCTION RUN HONAR [JEVDHYA VELA CLL KARNAR TEVDHYA VELES RUN HONAR]
hello()   # CALL KARYLA LAGT TEVHA FUNCTION RUN HONAR [JEVDHYA VELA CLL KARNAR TEVDHYA VELES RUN HONAR]
hello()   # CALL KARYLA LAGT TEVHA FUNCTION RUN HONAR [JEVDHYA VELA CLL KARNAR TEVDHYA VELES RUN HONAR]


def addition(a , b):          # A AND B ARE PARAMETER JUST LIKE A VARIBLE DEFINE KARNTYA SATHI

    print( a + b)

addition(13,15)      # 13 AND 15 ARE ARGUMENT TE AUTOMATICALY A AND B MADHI JANAR
addition(10000101,100)      # 13 AND 15 ARE ARGUMENT TE AUTOMATICALY A AND B MADHI JANAR
   
# PALLINDROM QUE


def palindrome_checker(a):
        
             
        copy = a

        rev = 0

        while a > 0:
          
          rev = rev * 10 + a % 10
          a = a // 10

        if rev == copy:
          print(f"{copy} IT IS A PALINDROME")

        else:
           print(f"{copy} NOT PALINDROME")

palindrome_checker(121)
palindrome_checker(787)
palindrome_checker(127)





# FUNCTION APPEOCH

# PRIVIOUS APPROCH IS PREMETIVE (YEK VARIBLE BANVNE TYACHYA VRR CH KAM KARNE)

# PARAMETERS AND ARGUMENT

# PARAMETERS ARE THE VALUES YOU ACCEPT WHILE
# CALLING THE FUCTION

# ARGUMENTS ARE THE VALUES YOU PROVIDES THE PARAMETERS
# WHILE CALLING THE FUNCTION



# POSITIONAL ARGUMENTS

def multiply(a,b,c,d):
    print(a * b * c * d)

multiply(12,15,66,11) # JEVDHE PARAMETER TEVHDE ARGUMENTS DENA


# DEFAULT ARGUMENT

def addition(a,b,c,d=12):
    print(a + b + c + d)

addition(12,22,22,)  # PARAMETER LA AGOTHER CH ARGUMENT DILAY def madhi


# KEYWORD ARGUMENT

def sub(a , b):
    print(a - b)

sub( b = 12 , a = 90)   #JRR B = 12 , DILLE AHE TRR SAGLYA SATHI SAME DYLA LAGEL


# RETURN 

def hello():
    return "how are you"

print(hello())