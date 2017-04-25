# Write a program to draw this. Assume the innermost square is 20 units per
# side, and each successive square is 20 units bigger, per side, than the one
# inside it.
import turtle

def create_window(color, title):
    """Creates a turtle window and returns it."""
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)

    return window

def create_turtle(color, pensize):
    """Creates a turtle object and returns it."""
    turtle_object =  turtle.Turtle()
    turtle_object.color(color)
    turtle_object.pensize(pensize)

    return turtle_object

def draw_square(turtle_object,length_of_side):
    """Draws 'number' square/s in the screen."""
    for j in range(4):              # draw square
        turtle_object.forward(length_of_side)
        turtle_object.left(90)

window = create_window("lightgreen", "squares")
pointer = create_turtle("pink", 5)

square_length = 20
for i in range(20):
    draw_square(pointer, square_length)
    square_length += 20

    pointer.penup()                 # adjust for the next square
    pointer.backward(10)
    pointer.right(90)
    pointer.forward(10)
    pointer.left(90)
    pointer.pendown()

window.mainloop()
