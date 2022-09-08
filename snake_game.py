from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
SPEED = 0.05 #0.0 is fastest 
screen = Screen()
screen.setup(1440, 900)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SPEED)
    snake.move()
    
    #detect collision with food
    if snake.head.distance(food) < 25:
        score.increase_score()
        food.refresh()
        snake.extend()
    #detect collision with wall 
    if snake.head.xcor() > 720 or snake.head.xcor() < -720 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        score.reset()
        snake.reset()
        
        
    #detect collision with tail    
    for segment in snake.segments[1:]: 
        if snake.head.distance(segment) < 10:  
            score.reset() 
            snake.reset()

screen.exitonclick()
