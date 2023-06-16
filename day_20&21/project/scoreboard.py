from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.show()

    def show(self):
        self.clear()
        self.write(f"Score : {self.score} High Score:{self.high_score}", False, align="center", font=('Arial', 12, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.show()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.pencolor("red")
    #     self.write("GAME OVER", False, align="center", font=('Arial', 16, 'normal'))