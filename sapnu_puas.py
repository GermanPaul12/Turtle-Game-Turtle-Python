import turtle
ALLIGNMENT = 'center'
FONT = ('Courier', 60, 'normal')
NAME = "Anjeza"

SPEED = 0 
screen = turtle.Screen()
screen.setup(1440, 900)
screen.bgcolor('black')
screen.title('Special Message')

def write_sapnu_puas():
    t = turtle.Turtle()
    t.color("white")
    t.hideturtle()
    t.write('sapnu puas', move=False, align=ALLIGNMENT, font=FONT)

guess = screen.textinput(title="The special greet", prompt="Enter a name" ).title()    
if guess == NAME:
    write_sapnu_puas()
screen.exitonclick()    
