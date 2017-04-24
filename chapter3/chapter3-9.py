# If you were going to draw a regular polygon with 18 sides, what
# angle would you need to turn the turtle at each corner?

# answer is: 20 degrees. 360 / 18 = 20.

import turtle

window = turtle.Screen()
pointer = turtle.Turtle()

pointer.penup()
pointer.left(-90)
pointer.forward(250)
pointer.left(90)
pointer.forward(-50)
pointer.pendown()

for i in range(18):
    pointer.forward(90)
    pointer.left(20)

window.mainloop()
