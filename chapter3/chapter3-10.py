# At the interactive prompt, anticipate what each of the following
# lines will do, and then record what happens. Score yourself,
# giving yourself one point for each one you anticipate correctly.

import turtle               # will import turtle
wn = turtle.Screen()        # creates a window
tess = turtle.Turtle()      # creates a turtle
tess.right(90)              # turtle will turn downwards
tess.left(3600)             # turtle will rotate left 10 times
tess.right(-90)             # turtle will turn left by 90 deg
tess.speed(10)              # turtle will speed down
# i'm wrong here (above line) actually, it seems that turtle will
# speed up. Here's the speedstrings for speed()
# fastest = 0, fast = 10, normal = 6, slow = 3, slowest = 1
# speed = 0 meeans no animation
tess.left(3600)             # turtle will rotate left 10 times
tess.speed(0)               # turtle will stop
tess.left(3645)             # turtle will stop
# if speed is equal to 0, it will instantly turn or move f/b
tess.forward(-100)          # turtle will stop
# like what will happen after executing this one

# final score: 8/12 haha

wn.mainloop()
