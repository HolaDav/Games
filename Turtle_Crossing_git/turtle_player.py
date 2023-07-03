from turtle import Turtle


class TurtlePlayer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.restart()

    def up(self):
        self.forward(10)

    def restart(self):
        self.goto(0, -280)
