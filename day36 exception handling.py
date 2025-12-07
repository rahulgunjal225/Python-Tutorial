# exception handling is the procces of responding to unwANTED AND unexcepted events when a computer programs run
# deals with a events to avoid the program or system crashing and without this process eception would disrupt the normal operation of a program
# try....except

a=input('enter the number: ')
print('multiplication table of {a} is:')
try:
   for i in range (1,11):
    print(f"{int(a)} x {i}={int(a)*i}")
except:
    print('invalid input')


print('some imp lines of code')
print('end of program')