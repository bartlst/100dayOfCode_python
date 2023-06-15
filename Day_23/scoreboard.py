from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.level = 0
        self.show()

    def show(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write("GAME OVER", False, align="center", font=FONT)
