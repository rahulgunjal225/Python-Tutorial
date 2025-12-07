import turtle

# Setup screen
wn = turtle.Screen()
wn.setup(500, 500)

# Create turtle
t = turtle.Turtle()
t.speed("fastest")

# Number of iterations
step = 100

# Draw squares in a spiral pattern
def draw_square(length, angle):
    for i in range(step):
        for b in range(4):
            t.forward(length + i)
            t.right(angle + b)  # Spiral effect

draw_square(100, 90)
wn.mainloop()
