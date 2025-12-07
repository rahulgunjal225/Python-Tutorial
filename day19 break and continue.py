# break statement
# the break statement enables a program to skip over a part of the code .
# a reak statement terminates the very loop it lies within




for i in range(12):
    if(i==10):
        break
    print("5x",i+1,"=",5* (i+1))




# continue statement
# the continue statement skip the rest of the loop statements and causes the next iteration too occur


for i in range(12):
    if(i==10):
        break
        print("2x",i+1,"=",2* (i+1))