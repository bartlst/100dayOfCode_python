from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score_l = 0
        self.score_r = 0
        self.show()

    def show(self):
        self.clear()
        self.write(f"{self.score_l}   :   {self.score_r}", False, align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write("GAME OVER", False, align="center", font=('Arial', 16, 'normal'))