# before we dive diffrence between local and global variables,lets first recall what a variable is in python
# a variable is a named location in amemory that store a value. in apython we can assign value to variable using a assignment operater
# a local variable tht defined with afunction and is only accesiable whithin that a function 
# a global variables is a varibale defined as outside of a function and is accessiable from within any function in you code

x=10 #global variable

def my_function():
    y=5 # local varibale
    print(y)



my_function()
print(x)
print(y)  # this will cause an error because y is a local a variable and is not accessible outside of the function