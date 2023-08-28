from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create the snake body
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
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






screen.exitonclick()