from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.show()

    def show(self):
        self.clear()
        self.write(f"Score : {self.score}", False, align="center", font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write("GAME OVER", False, align="center", font=('Arial', 16, 'normal'))