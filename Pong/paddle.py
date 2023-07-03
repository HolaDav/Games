from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position, 0)
        self.x_axis = self.xcor()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.x_axis, y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.x_axis, y=new_y)
