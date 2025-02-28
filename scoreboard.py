from turtle import Turtle

FONT = ("Courier", 20 , "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()

    def write_level(self):
        self.clear()
        self.goto(-260, 260)
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)


