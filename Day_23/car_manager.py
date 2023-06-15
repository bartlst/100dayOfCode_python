import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.spawn_car()
        self.move_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1,stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(x=300, y=random.randint(-240, 260))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.goto(car.xcor()-self.move_speed, car.ycor())

    def speed_increment(self):
        self.move_speed += MOVE_INCREMENT

