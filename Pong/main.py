from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(380)
l_paddle = Paddle(-380)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.up, "w")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < - 290:
        ball.bounce()

    if ball.distance(r_paddle) < 15 or ball.distance(l_paddle) < 15:
        ball.bounce()
        ball.increase_speed()

    if ball.xcor() > 390:
        scoreboard.add_r_score()
        ball.restart()

    elif ball.xcor() < -390:
        scoreboard.add_l_score()
        ball.restart()

screen.exitonclick()
