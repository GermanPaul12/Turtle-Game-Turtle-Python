from turtle import Turtle, Screen
import random
t = Turtle()
screen = Screen()


def moveforward():
    t.forward(10)
def moveleft():
    new_heading = t.heading() +10
    t.setheading(new_heading)
def moveright():
    new_heading = t.heading() -10
    t.setheading(new_heading)
def movebackward():
    t.backward(10)    
def random_color():
	screen.colormode(255)
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t.pencolor((r, g, b))
def clear_screen():
    t.home()
    t.clear()
             
def etch_sketch():
    t.shape('turtle')
    t.pensize(5)
    t.pencolor('white')
    t.write('Hello player.\n Press arrow keys to move\n Press c to clear everything \n Press r to change pencolor', move=False, align='left', font='Arial')
    t.speed(0)
    screen.bgcolor('black')
    t.color('blue')
    screen.onkey(fun=moveforward, key="Up") 
    screen.onkey(fun=moveleft, key="Left")
    screen.onkey(fun=moveright, key="Right")   
    screen.onkey(fun=movebackward, key="Down")
    screen.onkey(fun=random_color, key='r')
    screen.onkey(fun=clear_screen, key='c')
    screen.listen()
etch_sketch()    
screen.exitonclick()