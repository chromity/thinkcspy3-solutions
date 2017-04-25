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


def draw_poly(t, n, sz):
    """Will draw a polygon with 'n' sides each of them with length 'sz'."""
    for i in range(n):
        t.forward(sz)
        # turn left by 360 / number of sides degrees
        t.left(360 / n)


window = create_window("lightgreen", "pretty figure")
pointer = create_turtle("blue", 3)

pointer.penup()
pointer.backward(50)
pointer.pendown()

for i in range(20):
    draw_poly(pointer, 4, 100)
    pointer.right(360 / 20)

window.mainloop()
