# Write a program to draw a shape like this:
#   [image of star]

import turtle

window = turtle.Screen()
pointer = turtle.Turtle()

pointer.right(72)
for i in range(5):
    pointer.forward(100)
    pointer.right(144)

window.mainloop()
