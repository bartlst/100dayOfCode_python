from turtle import Turtle, Screen

adam = Turtle()

screen = Screen()


def move_forwards():
    adam.forward(10)

def move_backwards():
    adam.backward(10)


def trun_rignt():
    adam.left(10)


def trun_left():
    adam.right(10)


def clear():
    screen.reset()



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=trun_rignt)
screen.onkey(key="d", fun=trun_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
