import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()

screen.onkey(player.moveForward, "Up")
screen.listen()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    screen.update()

    cars.createNewCars()
    cars.moveCars()

    for car in cars.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()

    if player.touchedFinishLine():
        player.goToStart()
        cars.levelUp()

screen.exitonclick()
