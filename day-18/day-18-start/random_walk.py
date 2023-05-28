from turtle import Turtle, Screen
from random import choice, randint
import turtle

adam = Turtle()
turtle.colormode(255)
screen = Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    color = (red, blue, green)
    return color


angels = [0, 90, 180, 270]

adam.speed(0)
adam.width(10)
for _ in range(2000):
    adam.color(random_color())
    adam.forward(40)
    adam.setheading(choice(angels))
