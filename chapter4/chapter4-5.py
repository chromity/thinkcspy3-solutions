import turtle


def create_window(color, title):
    """Creates a turtle window and returns it."""
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)

    return window


def create_turtle(color, pensize):
    """Creates a turtle object and returns it."""
    turtle_object = turtle.Turtle()
    turtle_object.color(color)
    turtle_object.pensize(pensize)

    return turtle_object


window = create_window("lightgreen", "spirals")
pointer = create_turtle("blue", 3)

pointer.penup()
pointer.backward(170)
pointer.pendown()

pointer.speed(0)

# draw the first spiral
increment = 0
for i in range(51):
    pointer.right(90)
    pointer.forward(3 + increment)
    increment += 3

# position the pointer
pointer.penup()
pointer.backward(75)
pointer.right(90)
pointer.forward(350)
pointer.pendown()
pointer.right(90)

# draw the second spiral
increment = 0
for i in range(99):
    pointer.forward(3 + increment)
    pointer.right(89)
    increment += 3

window.mainloop()
