# a function in a block of code that performs a specific task whnever it is called is bigger program.
# when we have large amount of code it is advisied to creat or use existing function that make the program flow orginised and neat.


a=7
b=5
gmean=(a*b/(a+b))
print(gmean)




def calculategmean(a,b):
    gmean=(a*b)/(a+b)
    print(gmean)

a=6
b=3
calculategmean(a,b)

c=8
d=9
calculategmean(c,d)