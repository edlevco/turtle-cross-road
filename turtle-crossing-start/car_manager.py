from turtle import Turtle
from scoreboard import Scoreboard
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10





class CarManager():

    def __init__(self):
        self.allCars = []
        self.multiplier = 1

    def createCar(self):
        randNum = random.randint(1, 6)
        if randNum == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-225, 225))
            self.allCars.append(new_car)

    def moveCar(self):
        for car in self.allCars:
            car.backward(5 * self.multiplier)
            

    def nextLevel(self):
        self.multiplier += 1

        

    
    
   
    
