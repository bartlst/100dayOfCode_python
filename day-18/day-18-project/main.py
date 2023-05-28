import colorgram
import random
import turtle as t
colors = colorgram.extract('image.jpg', 10)
print(colors)

screen = t.Screen()
adam = t.Turtle()
adam.hideturtle()
t.colormode(255)
def random_color():
    color = random.choice(colors)

    return color.rgb

y_pos = -100
x_pos = -100
for row in range(10):
    adam.penup()
    y_pos += 50
    x_pos = -100
    for dot in range(10):
        x_pos += 50
        adam.setposition(x_pos, y_pos)
        adam.pendown()
        adam.dot(20, random_color())
        adam.penup()

adam.dot(20, random_color())
screen.exitonclick()

