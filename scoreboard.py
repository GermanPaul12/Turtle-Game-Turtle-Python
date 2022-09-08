from turtle import Turtle
ALLIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()   
        self.score = 0
        self.hideturtle()
        with open("/Users/german/Documents/Coding/Python projects/My coding projects/Turtle Library/Turtle Game/score.txt") as f:
            self.high_score = int(f.read())
        self.goto(0, 350)
        self.pencolor('white')
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score} High Score: {self.high_score}', move=False, align=ALLIGNMENT, font=FONT)
     
     
    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('/Users/german/Documents/Coding/Python projects/My coding projects/Turtle Library/Turtle Game/score.txt', mode='w') as f:
                f.write(f'{self.high_score}')
        self.score = 0 
        self.update_scoreboard()   
            
            
    #def game_over(self):
    #    self.goto(0,0)
    #    self.write('GAME OVER!', move=False, align=ALLIGNMENT, font=FONT)  
        
    def increase_score(self):
        self.score += 1    
        self.clear()
        self.write(f'Score : {self.score} High Score: {self.high_score}', move=False, align=ALLIGNMENT, font=FONT)
