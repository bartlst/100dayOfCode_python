from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SSSSSNAKE")
screen.tracer(0)
start_pos_x = 0
start_pos_y = 0

snake_squares = []
game_running = False

for _ in range(0, 3):
    snake_square = Turtle("square")
    snake_square.color("white")
    snake_square.penup()
    snake_square.goto(start_pos_x, start_pos_y)
    snake_squares.append(snake_square)
    start_pos_x -= 20

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    for square_num in range(len(snake_squares)-1, 0, -1):
        new_x = snake_squares[square_num-1].xcor()
        new_y = snake_squares[square_num-1].ycor()
        snake_squares[square_num].goto(new_x, new_y)

    snake_squares[0].forward(20)
    snake_squares[0].left(90)



