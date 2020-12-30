from turtle import Turtle
import random, time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        super(CarManager, self).__init__()
        self.allCars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createNewCars(self):
        randomCance = random.randint(1, 6)
        if randomCance == 1:
            newCar = Turtle("square")
            newCar.penup()
            newCar.shapesize(stretch_len=2, stretch_wid=1)
            newCar.color(random.choice(COLORS))
            randomY = random.randint(-250, 250)
            newCar.goto(300, randomY)
            self.allCars.append(newCar)

    def moveCars(self):
        for car in self.allCars:
            car.backward(self.carSpeed)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT

