from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):
    def __init__(self, starting_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=WIDTH/20, stretch_len=HEIGHT/20)
        self.penup()
        self.goto(starting_pos)
        self.setheading(90)

    def move_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
