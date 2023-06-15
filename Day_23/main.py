import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.onkey(key="space", fun=player.move)

trigger = True
counter = 0
game_is_on = True
while game_is_on:
    scoreboard.show()
    car_manager.move()
    time.sleep(0.1)
    counter += 1
    if counter == 6:
        car_manager.spawn_car()
        counter = 0
    if player.ycor() >= 265:
        scoreboard.level += 1
        car_manager.speed_increment()

    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()
    screen.update()


screen.exitonclick()