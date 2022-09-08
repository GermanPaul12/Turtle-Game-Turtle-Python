from turtle import Turtle, Screen
import random


screen = Screen()
screen.bgcolor('black')
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", 
                            prompt="Which turtle will win the race? You can choose from 'red', 'green', 'blue', 'yellow', 'orange', 'purple', 'white', 'cyan', 'magenta', 'gray'. Enter a color: ")
print(user_bet)

def goal_line():
    t = Turtle()
    t.penup()
    t.hideturtle()
    t.pensize(10)
    t.pencolor('red')
    t.goto(125, 100)
    t.right(90)
    t.pendown()
    t.forward(200)    
    
is_race_on = False  
all_turtles = []      
def create_race_turtles():
    goal_line()
    colors = ['red', 'orange', 'purple', 'white', 'cyan', 'green', 'blue', 'magenta', 'gray', 'yellow']
    ycor = [90,70,50,30,10,-10,-30,-50,-70,-90]
    for turtle_index in range(10):
        r = Turtle(shape='turtle')
        r.color(colors[turtle_index])
        r.penup()
        r.goto(-240, ycor[turtle_index])
        all_turtles.append(r)
    
    if user_bet:
        is_race_on = True 
    
    while is_race_on:  
        for i in all_turtles: 
            random_speed = random.randint(0, 10)
            i.forward(random_speed) 
            if i.xcor() > 125:
                is_race_on = False
                winning_color = i.pencolor()
                #print(f'Turtle {i.color()} won!')
                #is_race_on = False
                if user_bet == winning_color:
                    print(f'You betted on the {winning_color} turtle...you win!')
                else:
                    print(f'You betted on the wrong turtle...the winning turtle had the color {winning_color}!')    

       
        
create_race_turtles()

     
    
screen.exitonclick()