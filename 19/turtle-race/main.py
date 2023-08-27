import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Pick your turtle. Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def create_six_turtles():
    pos_x = -230
    pos_y = -70

    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(pos_x, pos_y)
        pos_y += 30
        turtles.append(new_turtle)


create_six_turtles()

if user_bet:
    is_race_on = True

winner = ""
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winner = turtle.color()[0]
            is_race_on = False
            if winner == user_bet:
                print(f"You've won. The {winner} turtle is the winner")
            else:
                print(f"You've lost. The {winner} turtle is the winner.")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
