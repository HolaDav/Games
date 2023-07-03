from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.angle = 50
        self.ball_speed = 10
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.start()

    def restart(self):
        self.ball_speed = 10
        if self.angle >= 140:
            self.angle = 50
            self.goto(0, 0)
            self.setheading(self.angle)
        else:
            self.angle = self.angle + 90
            self.goto(0, 0)
            self.setheading(self.angle)

    def start(self):
        self.setheading(self.angle)

    def move(self):
        self.forward(self.ball_speed)

    def bounce(self):
        new_heading = self.heading() - 90
        self.setheading(new_heading)
        self.move()

    def increase_speed(self):
        self.ball_speed += 1
