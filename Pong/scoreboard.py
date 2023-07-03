from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Right:{self.r_score}     Left:{self.l_score}", align="center", font=("courier", 20, "normal"))

    def add_r_score(self):
        self.clear()
        self.r_score += 1
        self.write(f"Right:{self.r_score}     Left:{self.l_score}", align="center", font=("courier", 20, "normal"))

    def add_l_score(self):
        self.clear()
        self.l_score += 1
        self.write(f"Right:{self.r_score}     Left:{self.l_score}", align="center", font=("courier", 20, "normal"))