# FUNCTION LA SHORT MADHI LIHNYA SATHI

def check(a):
    if a % 2==0:
        print("even number")
    else:
        print("odd number")

check(12)


check = lambda x: print("even number") if x %2 ==0 else print("odd number")

check(12)




addition = lambda a,b : a+b

print(addition(10,20))