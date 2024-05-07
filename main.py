import turtle


# Function to draw fractal tree
def draw_fractal_tree(branch_length, t):
    if branch_length < 10:
        return
    else:
        t.forward(branch_length)
        t.left(30)
        draw_fractal_tree(branch_length * 0.7, t)
        t.right(60)
        draw_fractal_tree(branch_length * 0.7, t)
        t.left(30)
        t.backward(branch_length)

        # Return to the original position
        t.forward(branch_length)


# Set up the screen

screen = turtle.Screen()
screen.title("Fractal Tree Generator")
screen.setup(width=80, height=800)

# Create an instance for the turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -50)
t.pendown()

# Set initial parameters
branch_length = 100

# Draw the fractal tree
draw_fractal_tree(branch_length, t)

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()
