from turtle import Turtle
import random

STARTSPEED = 10
SPEEDUP =10
COLOUR =  [ "Orange", "Yellow", "Green", "Blue", "Indigo", "black"]

class Car:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTSPEED

    def create_car(self):
        if random.randint(1,7) ==2:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOUR))
            y_ran = random.randint(-250,250)
            new_car.goto(300, y_ran)
            self.cars.append(new_car)


    def move(self):
        for car in self.cars:
             car.backward(self.car_speed)


    def level_up(self):
        self.car_speed+=SPEEDUP

   #
    # def move(turtle):
    #     for car in cars:
    #         car.backward(10)