import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()



screen.onkey(key="Up", fun=player.forward)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.createCar()
    car_manager.moveCar()

    for car in car_manager.allCars:
        if car.distance(player) < 20 and car.ycor() - player.ycor() < 20:
            scoreboard.gameOver()
            game_is_on = False
            break


    if player.ycor() > 280:
        scoreboard.increaseScore()
        car_manager.nextLevel()
        player.reset()
    


screen.exitonclick()
