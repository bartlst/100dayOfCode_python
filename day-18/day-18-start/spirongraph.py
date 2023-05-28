from turtle import Turtle, Screen
from random import choice, randint
import turtle

adam = Turtle()
turtle.colormode(255)
screen = Screen()
adam.width(1)
adam.speed(0)

def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    color = (red, blue, green)
    return color


def draw_spinograph(t, circle_num):
    angle = 360/circle_num
    for _ in range(circle_num):
        t.color(random_color())
        t.circle(100)
        t_heading = t.heading()
        t.setheading(t_heading + angle)


draw_spinograph(adam, 88)
screen.exitonclick()
