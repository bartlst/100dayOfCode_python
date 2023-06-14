from turtle import Turtle

WIDTH = 20
HEIGHT = 20


class Ball(Turtle):
    def __init__(self, starting_pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_wid=WIDTH/20, stretch_len=HEIGHT/20)
        self.penup()
        self.goto(starting_pos)
        self.x_move = 7
        self.y_move = 7

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
