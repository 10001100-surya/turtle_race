from turtle import Turtle, Screen

FONT = ("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(-270, 250)
        self.write(f"level:{self.level}", align="left", font=FONT)

    def inc_score(self):
        self.clear()
        self.level+=1
        self.update_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)