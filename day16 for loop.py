# sometimes a programer wants to execute a group of statements a certain number of times .this can be done using loops 
#based on this loops are further classified into folloeing types for loop,while loop,nested loop


name='abhishek'
for i in name:
    print(i)
    if(i=='b'):
        print("this is something special")

color=["red","pink",'yellow',"blue"]
for color in color:
    print(color)
    for i in color:
        print(i)


#range function


for r in range (111111):
    print(r+1)