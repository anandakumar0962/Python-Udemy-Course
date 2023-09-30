from turtle import Turtle, Screen
colors = ['blue', 'cyan', 'DeepPink', 'DarkGreen', 'DarkRed', 'red', 'orange', 'purple']
sides = [i for i in range(3, 11)]
turtle = Turtle()
turtle.shape("turtle")

def draw_shapes(no_of_sides, color):
    turtle.pensize(3)
    turtle.color(color)
    for _ in range(no_of_sides):
        angel = 360//no_of_sides
        turtle.forward(100)
        turtle.right(angel)

for i, j in zip(sides, colors):
    draw_shapes(i,j)


    






screen = Screen()
screen.exitonclick()