# Suppose our turtle tess is at heading 0 - facing east. We execute the
# statement tess.left(3645). What does tess do, and what is her final heading?

import turtle

window = turtle.Screen()
tess = turtle.Turtle()

tess.left(3645)
# if tess is heading at 0, facing east, then she will be still be heading at 0
# but facing 45 degrees to the left now. (after she will also rotate by 10x)
