# Write a program to draw a face of a clock that looks something like this

import turtle

board = turtle.Screen()
pointer = turtle.Turtle()

for i in range(12):
    pointer.right(30)       # turn the pointer to the right

    pointer.penup()         # traverse without leaving a mark
    pointer.forward(100)

    pointer.pendown()       # leave a streak of line
    pointer.forward(20)

    pointer.penup()         # traverse a little without leaving a mark
    pointer.forward(15)

    pointer.pendown()       # put a pointer mark
    pointer.stamp()

    pointer.penup()         # go back to starting point
    pointer.forward(-135)

board.mainloop()            # wait for the user to close the window
