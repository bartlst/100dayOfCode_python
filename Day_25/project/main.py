import turtle
import pandas
import time


score = 0

screen = turtle.Screen()
screen.title("State game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_answers = []

def show_sate(state_data):
    t = turtle.Turtle()
    t.penup()
    x = int(state_data['x'])
    y = int(state_data['y'])
    t.goto(x,y)
    t.write(state_data.state.item())


data = pandas.read_csv('50_states.csv')
game_running = True

while game_running:
    time.sleep(1)
    user_guest = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")

    if user_guest in data['state'].unique() and user_guest not in correct_answers:
        score += 1
        correct_answers.append(user_guest)
        state = (data[data['state'] == user_guest])
        show_sate(state)
    else:
        print("No")
    if score == 50:
        game_running = False

screen.exitonclick()