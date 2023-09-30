from turtle import Turtle, Screen
import random
colors = ['blue', 'cyan', 'DeepPink', 'DarkGreen', 'DarkRed', 'red', 'orange', 'purple']
turtle = Turtle()
directions = [0, 90, 180, 270]
turtle.pensize(10)
turtle.speed(0)

def random_walk(color, direction):
    turtle.color(color)
    turtle.forward(25)
    turtle.setheading(direction)

for _ in range(250):
    
    random_walk(random.choice(colors), random.choice(directions))









screen = Screen()
screen.exitonclick()