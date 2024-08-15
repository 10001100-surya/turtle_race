from turtle import Turtle
import random
MOVEDISTANCE = 10
STARTING_POSITION = (0,-280)

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move_up(self):
        self.forward(MOVEDISTANCE)

    def move_down(self):
        self.backward(MOVEDISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVEDISTANCE)
        self.setheading(90)


    def move_right(self):
        self.setheading(0)
        self.forward(MOVEDISTANCE)
        self.setheading(90)

    def gotostart(self):
        self.goto(STARTING_POSITION)