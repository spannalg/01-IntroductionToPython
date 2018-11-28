"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Luke Spannan
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
turtle_one = rg.SimpleTurtle('turtle')
turtle_one.pen = rg.Pen('Red',5)
turtle_one.speed = 15
size = 120
for k in range(12):
    turtle_one.draw_circle(size)
    turtle_one.pen_up()
    turtle_one.right(30)
    turtle_one.pen_down()
    size = size - 5
turtle_two = rg.SimpleTurtle('turtle')
turtle_two_pen = rg.Pen('Green',10)
turtle_two.forward(5)
turtle_two.speed = 10
for k in range(8):
    turtle_two.draw_square(200)
    turtle_two.pen_up()
    turtle_two.left(45)
    turtle_two.pen_down()
