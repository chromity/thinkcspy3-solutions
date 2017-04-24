# Use for loops to make a turtle draw these regular polygons
# (regular means all sides the same lengths, all angles the
# the same):
#   * An equilateral triangle
#   * A square
#   * A hexagon (six sides)
#   * An octagon (eight sides)

import turtle

window = turtle.Screen()        # instantiate a window
pointer = turtle.Turtle()       # instantiate a turtle

pointer.penup()                 # lift the turtle to avoid mark
pointer.forward(-200)           # go left by 200 units
pointer.pendown()               # lift the turtle down

# drawing an equilateral triangle
for i in range(3):
    pointer.forward(50)
    pointer.left(120)  # 3 angles so 360 / 3 = 120

# put a space between the figures
pointer.penup()
pointer.forward(100)
pointer.pendown()

# drawing a square
for i in range(4):
    pointer.forward(50)
    pointer.left(90)    # 4 angles so 360 / 4 = 90

pointer.penup()
pointer.forward(120)
pointer.pendown()

# drawing a hexagon
for i in range(6):
    pointer.forward(30)
    pointer.left(60)    # 6 angles so 360 / 6 = 60

pointer.penup()
pointer.forward(120)
pointer.pendown()

# drawing an octagon
for i in range(8):
    pointer.forward(25)
    pointer.left(45)    # 360 / 8 = 45


window.mainloop()       # wait for user to close the window
