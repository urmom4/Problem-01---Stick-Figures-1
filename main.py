
#import stuff from prgame plus library
from pygameplus import *

screen = Screen(575, 400, "my graphics program")
screen.open()
screen.background_color = "sky blue"
screen.redraw()

michael = Turtle()
screen.add(michael)

#make michael draw the first stick figure
Turtle.line_width = 4
michael.fill_color = 'black'
michael.begin_line()

michael.turn_left(105)
michael.move_forward(50)
michael.turn_left(155)
michael.move_forward(50)
michael.end_line

michael.turn_right(180)
michael.move_forward(50)
michael.turn_left(10)

michael.begin_line()
michael.move_forward(50)
michael.end_line()
michael.turn_right(90)
michael.begin_line()
michael.circle(15)
michael.turn_right(90)
michael.move_forward(10)
michael.turn_left(45)
michael.move_forward(35)
michael.turn_left(180)
michael.move_forward(35)
michael.turn_left(90)
michael.move_forward(35)
michael.end_line()
michael.turn_left(180)
michael.move_forward(35)
michael.turn_right(90)
michael.move_forward(35)
michael.turn_left(45)
michael.move_forward(50)
michael.begin_line()
michael.circle(8)
michael.move_forward(16)
michael.circle(20)
michael.turn_left(90)
michael.end_line()
michael.move_forward(18)
michael.begin_fill()
michael.circle(4)
michael.end_fill()
michael.turn_left(180)
michael.move_forward(16)
michael.turn_left(45)
michael.begin_line()
michael.move_forward(50)
michael.turn_right(180)
michael.move_forward(25)
michael.turn_left(90)
michael.move_forward(25)
michael.turn_left(180)
michael.move_forward(25)
michael.turn_right(45)
michael.move_forward(50)
michael.turn_right(45)
michael.move_forward(25)
michael.turn_left(180)
michael.move_forward(25)
michael.turn_left(90)
michael.move_forward(25)
michael.turn_left(180)
michael.move_forward(50)
michael.turn_left(180)
michael.circle(4)

#make the shape for part 3 of the priject
michael.end_line()
michael.turn_right(135)
michael.move_forward(90)
michael.turn_left(90)
michael.move_forward(400)
michael.begin_fill()
michael.fill_color = "yellow"
michael.circle(25)