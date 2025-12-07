# recursion is the process of defining something in terms of itself
#  in python, we known that a function call other function 
# it is a even possible for thr function to call itself 
# these type of construct are termed as recursive function

#  function chya Aatmdhlya function la call karne tyala recursion mhanatat


# factorial(7)=7*6*5*4*3*2*1*
# factorial(6)=6*5*4*3*2*1*
# factorial(5)=5*4*3*2*1*
# factorial(0)=1


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_win.setup(500,500)

def draw_spiral(my_turtle, line_len):
    if line_len <=0:             # works till length is greater than 0
        return
    else:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle,line_len-10)   # recursive call

draw_spiral(my_turtle,160)

#Write the logic to take the turtle to its destination
#Refer the statements given above to draw the pattern

#Provide different values and test your program
destination="south"


