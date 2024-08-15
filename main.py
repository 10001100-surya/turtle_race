import random
from turtle import Turtle,Screen
from player import Player
from car import Car
from random import Random
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("turtle race")
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.tracer(0)


player = Player()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down,"Down")
screen.onkeypress(player.move_left,"Left")
screen.onkeypress(player.move_right,"Right")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    for _ in car.cars:
        if _.distance(player) < 22:
            scoreboard.game_over()
            game_on = False
        if player.ycor() == 280:
            player.gotostart()
            car.level_up()
            scoreboard.inc_score()

screen.exitonclick()