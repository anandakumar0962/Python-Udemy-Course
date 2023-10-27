import turtle, pandas
from location_pointer import LocationPointer

location = LocationPointer()


screen = turtle.Screen()
screen.title("U.S. State Game")
image = "/0 Udemy/Python/Projects/Day 21 - 30/Day 25/U.S. State Game/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

datas = pandas.read_csv("C:/0 Udemy/Python/Projects/Day 21 - 30/Day 25/U.S. State Game/day-25-us-states-game-start/50_states.csv")
STATES = datas.state.to_list()

marked_states = []
while len(marked_states) < len(STATES):
    answer_data = screen.textinput(title=f'{len(marked_states)}/50 Guess US State', prompt="What's another state?").title()
    if answer_data == 'Exit':
        missed_states = [state for state in STATES if state not in marked_states]
        to_learn = pandas.DataFrame(missed_states)
        to_learn.to_csv("States_to_learn.csv")
        break
    if answer_data in STATES:
        location_data = datas[datas.state == answer_data]
        location.location_pointer(answer_data, int(location_data.x), int(location_data.y))
        marked_states.append(answer_data)


    
    


