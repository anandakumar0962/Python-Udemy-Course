from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width= 500, height=400)
user_choice = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter the color: ").lower()
if user_choice:
    is_race_on = True
colors = ['red', "yellow", "green", 'blue', "orange"]
y_position = [-60, -30, 0, 30, 60]
turtles = []
for i in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_position[i])
    turtles.append(new_turtle)


while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_choice:
                print(f"You won! The {winning_color} turtle won the race.")
            else:
                print(f"You lost! The {winning_color} turtle won the race.")
        forward_pos = random.randint(0,10)
        turtle.forward(forward_pos)

screen.exitonclick()