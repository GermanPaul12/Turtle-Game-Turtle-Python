from turtle import Turtle, Screen
import random
from color import colors
screen = Screen()
screen.bgcolor('black')
patrick_the_turtle = Turtle()
patrick_the_turtle.shape('turtle')
patrick_the_turtle.color('blue')
patrick_the_turtle.pencolor('yellow')
def square():
	patrick_the_turtle.home()
	patrick_the_turtle.forward(100)
	patrick_the_turtle.left(90)
	patrick_the_turtle.forward(100)
	patrick_the_turtle.left(90)
	patrick_the_turtle.forward(100)
	patrick_the_turtle.left(90)
	patrick_the_turtle.forward(100)
	patrick_the_turtle.left(90)
def dashed_line(z):
	for i in range(z):
		patrick_the_turtle.forward(10)
		patrick_the_turtle.penup()
		patrick_the_turtle.forward(10)
		patrick_the_turtle.pendown()
		patrick_the_turtle.forward(10)
def dashed_structure(): 
	patrick_the_turtle.penup()
	dashed_line(10)
	patrick_the_turtle.pendown()
	patrick_the_turtle.left(90) 
	dashed_line(10)
	patrick_the_turtle.left(90)
	dashed_line(10)
	dashed_line(10)
	patrick_the_turtle.left(90)
	dashed_line(10)
	dashed_line(10)
	patrick_the_turtle.left(90)
	dashed_line(10)
	dashed_line(10)
	patrick_the_turtle.left(90)
	dashed_line(5)
	patrick_the_turtle.left(90)
	dashed_line(5)

def mixed_structure():
	patrick_the_turtle.pencolor(random.choice(colors))
	mixed_structure_triangle()
	patrick_the_turtle.pencolor(random.choice(colors))
	mixed_structure_square()
	patrick_the_turtle.pencolor(random.choice(colors))
	mixed_structure_pentagon()
	patrick_the_turtle.pencolor(random.choice(colors))
	mixed_structure_hexagon()
	patrick_the_turtle.pencolor(random.choice(colors))
	mixed_structure_heptagon()
	patrick_the_turtle.pencolor(random.choice(colors))
	mixed_structure_octagon()
	patrick_the_turtle.pencolor(random.choice(colors))
	mixed_structure_nonagon()
	patrick_the_turtle.pencolor(random.choice(colors))
	mixed_structure_decacon()

def mixed_structure_triangle():
	for i in range(3):
		patrick_the_turtle.right(120)
		patrick_the_turtle.forward(100)

def mixed_structure_square():
	for i in range(4):
		patrick_the_turtle.right(90)
		patrick_the_turtle.forward(100)

def mixed_structure_pentagon():
	for i in range(5):
		patrick_the_turtle.right(72)
		patrick_the_turtle.forward(100)    


def mixed_structure_hexagon():
	for i in range(6):
		patrick_the_turtle.right(60)
		patrick_the_turtle.forward(100)
		
def mixed_structure_heptagon():   
	for i in range(7):
		patrick_the_turtle.right(51.4285714)     
		patrick_the_turtle.forward(100)
		
		
def mixed_structure_octagon():
	for i in range(8):
		patrick_the_turtle.right(45)
		patrick_the_turtle.forward(100)
		

def mixed_structure_nonagon():
	for i in range(9):
		patrick_the_turtle.right(40)
		patrick_the_turtle.forward(100)
		

def mixed_structure_decacon():
	for i in range(10):
		patrick_the_turtle.right(36)   
		patrick_the_turtle.forward(100)     
			   

def random_color():
	screen.colormode(255)
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	patrick_the_turtle.pencolor((r, g, b))

def randomized_walk():
	angles = [90, 180, 270, 360]
	length = [5, 10, 15, 20, 25, 30]
	patrick_the_turtle.speed(0)
	patrick_the_turtle.pensize(4)
	for i in range(10000):
		random_color()
		random_angles = random.choice(angles)
		patrick_the_turtle.setheading(random_angles)
		random_length = random.choice(length)
		patrick_the_turtle.forward(random_length)

def spirograph():
	patrick_the_turtle.penup()
	patrick_the_turtle.speed(0)
	patrick_the_turtle.goto(0, -300)
	for i in range(360):
		random_color()
		patrick_the_turtle.circle(300, 1)
		patrick_the_turtle.pendown()
		patrick_the_turtle.circle(50)
		

#spirograph()
randomized_walk()

screen.exitonclick()