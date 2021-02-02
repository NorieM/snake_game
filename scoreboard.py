from turtle import Turtle

WRITE_SETTINGS = {'align': 'center',
                  'font': ('Arial', 20, 'normal')
                  }


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align=WRITE_SETTINGS['align'], font=WRITE_SETTINGS['font'])

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=WRITE_SETTINGS['align'], font=WRITE_SETTINGS['font'])