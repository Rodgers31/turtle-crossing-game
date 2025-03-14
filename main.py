import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()
    scoreboard.write_level()

#     Detect collision with car
    for one_car in car.all_cars:
        if one_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

# Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car.leve_up()
        scoreboard.increase_level()

screen.exitonclick()