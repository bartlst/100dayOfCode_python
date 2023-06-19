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
remaining_states = []
data_dict={
    'state' : [],
    'x':[],
    'y':[]
}

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
    user_guest = user_guest.title()
    if user_guest in data['state'].unique() and user_guest not in correct_answers:
        score += 1
        correct_answers.append(user_guest)
        state = (data[data['state'] == user_guest])
        show_sate(state)

    if user_guest == "Exit":
        game_running = False
    if score == 50:
        game_running = False

remaining_states = [state_name for state_name in data['state'].to_list() if state_name not in correct_answers]


for state_name in remaining_states:
    data_dict['state'].append(data[data['state'] == state_name].state.item())
    data_dict['x'].append(data[data['state'] == state_name].x.item())
    data_dict['y'].append(data[data['state'] == state_name].y.item())


final_data = pandas.DataFrame(data_dict)
final_data.to_csv('new_csv.csv')
print(data_dict)
screen.exitonclick()