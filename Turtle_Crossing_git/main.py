from turtle import Screen
from car_manager import CarManager
from turtle_player import TurtlePlayer
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

car_manager = CarManager()
turtle_player = TurtlePlayer()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle_player.up, "Up")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move()

    if turtle_player.ycor() > 300:
        turtle_player.restart()
        scoreboard.level_up()
        car_manager.increase_speed()

    for car in car_manager.car_list:
        if turtle_player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
