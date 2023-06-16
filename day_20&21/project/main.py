from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_running = True
while game_running:
    scoreboard.show()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.squares[0].distance(food) < 18:
        food.refresh()
        scoreboard.score += 1
        snake.extend()

    # detect collision with wall
    if snake.squares[0].xcor() > 285 or snake.squares[0].xcor() < -285 or \
            snake.squares[0].ycor() > 285 or snake.squares[0].ycor() < -285:
        scoreboard.reset()
        snake.reset()

    # detect collision with wall
    for square in snake.squares[1:]:
        if snake.squares[0].distance(square) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
