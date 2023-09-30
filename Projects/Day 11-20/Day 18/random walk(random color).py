import turtle as t
import random
turtle = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]
turtle.pensize(10)
turtle.speed(0)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

def random_walk(direction):
    turtle.color(random_color())
    turtle.forward(25)
    turtle.setheading(direction)

for _ in range(250):
    
    random_walk(random.choice(directions))


screen = t.Screen()
screen.exitonclick()