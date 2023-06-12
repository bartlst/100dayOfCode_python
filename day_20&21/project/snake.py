from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_square = Turtle("square")
            snake_square.color("white")
            snake_square.penup()
            snake_square.goto(position)
            self.squares.append(snake_square)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.squares[0].heading() != 270:
            self.squares[0].setheading(90)

    def down(self):
        if self.squares[0].heading() != 90:
            self.squares[0].setheading(270)

    def right(self):
        if self.squares[0].heading() != 180:
            self.squares[0].setheading(0)

    def left(self):
        if self.squares[0].heading() != 0:
            self.squares[0].setheading(180)
