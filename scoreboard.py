from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increaseLevel(self):
        self.level += 1
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
