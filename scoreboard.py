from turtle import Turtle

WRITE_SETTINGS = {'align': 'center',
                  'font': ('Arial', 20, 'normal')
                  }
DATA_FILE = 'data.txt'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
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
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=WRITE_SETTINGS['align'], font=WRITE_SETTINGS['font'])

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.show_score()

    def read_high_score(self):
        with open(DATA_FILE) as file:
            return int(file.read())

    def write_high_score(self):
        with open(DATA_FILE, mode='w') as file:
            file.write(str(self.high_score))