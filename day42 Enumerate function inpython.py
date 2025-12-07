# the enumerate function is a built in function in python that allows you to loop over a sequence
# (such as a lsit,tuple,string) and the get the index and value of each element in the sequence at the same time



marks=[10,22,34,88,99,2,13,5]
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("rahul,nice!")