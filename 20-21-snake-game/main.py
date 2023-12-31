from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create the snake body
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

# move the snake
game_is_on = True
while game_is_on:
    # updates screen every 0.1 seconds
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if (
        snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    tail = snake.segments[1:]
    for segment in tail:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
