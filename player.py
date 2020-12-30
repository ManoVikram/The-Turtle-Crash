from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.goToStart()

    def moveForward(self):
        self.forward(MOVE_DISTANCE)

    def goToStart(self):
        self.goto(STARTING_POSITION)

    def touchedFinishLine(self):
        if self.ycor() == FINISH_LINE:
            return True
        else:
            return False
