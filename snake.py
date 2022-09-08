from turtle import Turtle
import random
from color import colors
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SIZE = 1.2 #1 is normal 0.5 is half the size and so on

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.extend_snake(i)
            
            
    def extend_snake(self, position):
        t = Turtle()
        random_color = random.choice(colors)
        t.color(random_color)
        t.shape('square')
        t.turtlesize(SIZE)
        t.penup()
        t.goto(position)
        self.segments.append(t)   
        
    def extend(self):
        self.extend_snake(self.segments[-1].position())         
        
    def reset(self):
        for _ in self.segments:
            _.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()     
        self.head = self.segments[0]   
            
    def move(self):
          
        for seg_num in range(len(self.segments) -1, 0, -1):  
            next_x = self.segments[seg_num -1].xcor()
            next_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(next_x, next_y)
        self.head.forward(MOVE_DISTANCE)         
        
        
    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)     

        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  

        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  
