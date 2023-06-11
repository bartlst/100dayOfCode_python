import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=400)

user_bet = screen.textinput(title="Set your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

race = False
colors = ["red", "orange", "yellow", "blue", "purple"]
turtles = []
start_pos_x = -280
start_pos_y = -60

for index in range(len(colors)):
    new_adam = Turtle(shape="turtle")
    new_adam.penup()
    new_adam.color(colors[index])
    new_adam.goto(start_pos_x, start_pos_y)
    start_pos_y += 30
    turtles.append(new_adam)

if user_bet:
    race = True

while race:
    distance = random.randint(0, 10)
    turtle = random.choice(turtles)
    turtle.forward(distance)
    print(turtle.position()[0])
    if turtle.position()[0] >= (screen.window_width()/2)-10:
        winner = turtle.pencolor()
        race = False
        if user_bet == winner:
            print(f"{winner} turtle won, you ware correct!")
        else:
            print(f"{winner} turtle won, you ware wrong.")


screen.exitonclick()
