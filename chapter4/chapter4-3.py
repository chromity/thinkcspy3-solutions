# Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular
# polygon.

import turtle


def draw_poly(t, n, sz):
    """Will draw a polygon with 'n' sides each of them with length 'sz'."""
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)           # turn left by 360 / number of sides degrees


window = turtle.Screen()
pointer = turtle.Turtle()

draw_poly(pointer, 8, 50)       # draw the polygon

window.mainloop()
