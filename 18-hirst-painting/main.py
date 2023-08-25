import random
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]

cookie = Turtle()
cookie.hideturtle()
cookie.penup()

x = -200
y = -200
cookie.setx(x)
cookie.sety(y)

for i in range(1, 11):
    for j in range(10):
        cookie.dot(20, random.choice(color_list))
        cookie.forward(50)
    y += 50
    cookie.setx(x)
    cookie.sety(y)





screen = Screen()
screen.exitonclick()