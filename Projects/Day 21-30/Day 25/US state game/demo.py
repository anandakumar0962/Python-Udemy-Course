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

score = 0

for answer_data in STATES:
    location_data = datas[datas.state == answer_data]
    x_cor = location_data.x.to_list()
    y_cor = location_data.y.to_list()
    location.location_pointer(answer_data, *x_cor, *y_cor)
    score+=1


    
    

screen.exitonclick()
