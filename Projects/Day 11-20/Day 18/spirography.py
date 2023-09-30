import turtle as t
import random
turtle = t.Turtle()
t.colormode(255)
turtle.speed(0)
turtle.pensize(3)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

def spirography(size):
    for _ in range(360//size):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size)

spirography(5)


screen = t.Screen()
screen.exitonclick()