# Draw five stars, but between each, pick up the pen, move forward by 350 units
# turn right by 144, put the pen down, and draw the next star. You'll get
# something like this:

import turtle

def draw_star(t):
    """Draws a star having sides of 100 units in length."""
    for i in range(5):
        t.forward(100)
        t.right(144)


window = turtle.Screen()
pointer = turtle.Turtle()

pointer.penup()         # adjust the init pos of the turtle
pointer.backward(180)
pointer.left(90)
pointer.forward(100)
pointer.right(90)
pointer.pendown()

for i in range(5):
    draw_star(pointer)
    pointer.penup()
    pointer.forward(350)
    pointer.right(144)
    pointer.pendown()

window.mainloop()
