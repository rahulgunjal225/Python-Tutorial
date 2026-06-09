
#  : Write a program to find whether a given username contains less than 10 
#  : characters or not. 

username  = input('Enter the username : ')

if(len(username)<10):
    print(" your username contains less than 10 caracters")

else:
    print('your username contains more than or equal to 10 characters')