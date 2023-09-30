from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

#Setup screen.
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(380, 0)
left_paddle = Paddle(-380, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.up,"Up" )
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle.
    if (ball.distance(right_paddle) < 50 and ball.xcor()>350) or (ball.distance(left_paddle)<50 and ball.xcor()<-350):
        ball.bounce_x()

    #Detect right player miss ball:
    if ball.xcor()> 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect left player miss ball.
    if ball.xcor()< -380:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()