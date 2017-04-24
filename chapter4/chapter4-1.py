# Write a void (non-fruitful) function to draw a square. Use it in a program
# to draw the image shown below. Assume each side is 20 units. (Hint: notice
# that the turtle has already moved away from the ending point of the last
# square when the program ends)

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

def draw_square(turtle_object, number, length_of_side):
    """Draws 'number' square/s in the screen."""
    for i in range(number):
        for j in range(4):          # draw square
            turtle_object.forward(length_of_side)
            turtle_object.left(90)

        turtle_object.penup()       # put a space for the next square
        turtle_object.forward(40)
        turtle_object.pendown()

window = create_window("lightgreen", "squares")
pointer = create_turtle("pink", 5)

pointer.penup()                     # to centerize the squares
pointer.forward(-100)
pointer.pendown()

draw_square(pointer, 5, 20)

window.mainloop()
