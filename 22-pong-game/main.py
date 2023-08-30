from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
# turn of animation
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    # to show the paddle
    time.sleep(0.05)
    ball.move()

    # detect collision top - bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    # right_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    screen.update()

screen.exitonclick()
