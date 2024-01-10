from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-250, 250)
        self.write(f"Level: {self.score}", align="left", font=FONT)
    
    def increaseScore(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def gameOver(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)






