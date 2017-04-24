# Enhance your program above (see chapter3-7.py) to tell us what the
# drunk pirate's heading is after he has finished stumbling around.
# (Assume he begins at heading 0).

import turtle

sea = turtle.Screen()           # sea, hahaha.
drunk_pirate = turtle.Turtle()  # turate, a turtle pirate.

direction = 0
for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    drunk_pirate.left(i)        # if negative, it will turn right
    drunk_pirate.forward(100)
    direction += i

direction %= 360
print("Our friend's position is %d deg left of east" % direction)

sea.mainloop()                  # wait for user to close the window
