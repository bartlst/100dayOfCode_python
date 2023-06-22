import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((270, 0))
l_paddle = Paddle((-270, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)


screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_on = True
game_speed = 0.1
while game_on:
    time.sleep(game_speed)
    scoreboard.show()
    ball.move()
    screen.update()

    # detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 45 and ball.xcor() > 250:
        ball.bounce_x()
        game_speed /= 1.2
    if ball.distance(l_paddle) < 45 and ball.xcor() < -250:
        ball.bounce_x()
        game_speed /= 1.2

    # ball out of the screen
    if ball.xcor() > 280:
        ball.reset_position()
        scoreboard.score_l += 1
        game_speed = 0.1

    if ball.xcor() < -280:
        ball.reset_position()
        scoreboard.score_r += 1
        game_speed = 0.1




screen.exitonclick()