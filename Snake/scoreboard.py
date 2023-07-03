from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 30, "normal")
GAME_OVER_FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !!!", align=ALIGN, font=GAME_OVER_FONT)
