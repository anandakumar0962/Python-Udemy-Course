from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(xcor, ycor)

    def up(self):
        new_y_cor = self.ycor()+20
        self.goto(self.xcor(), new_y_cor)

    def down(self):
        new_y_cor = self.ycor()-20
        self.goto(self.xcor(),new_y_cor)