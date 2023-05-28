from turtle import Turtle, Screen
from random import choice

adam = Turtle()

screen = Screen()
# for _ in range(4):
#     adam.forward(50)
#     adam.left(90)
#
# screen.clear()
# for _ in range(15):
#     adam.forward(15)
#     if adam.isdown():
#         adam.penup()
#     else:
#         adam.pendown()
colors = ['red', 'brown', 'orange', 'pink', 'green', 'black']


def draw(turtle, num_sides, size, color):
    angle = 360/num_sides
    turtle.pencolor(color)
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(angle)


adam.speed(60)
for num in range(3, 30):
    draw(adam, num, 20, choice(colors))
adam.forward(30)
adam.right(180)
for num in range(3, 30):
    draw(adam, num, 20, choice(colors))

screen.exitonclick()
