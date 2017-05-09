# Write a void function to draw a star, where the length of each side is 100
# units. (Hint: You should turn the turtle by 144 degrees at each point.)

import turtle


def draw_star(t):
    """Draws a star having sides of 100 units in length."""
    for i in range(5):
        t.forward(100)
        t.right(144)


window = turtle.Screen()
pointer = turtle.Turtle()

draw_star(pointer)

window.mainloop()
