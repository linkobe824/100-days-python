from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# Create the snake body
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        pos_x = 0
        for i in range(3):
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.goto(pos_x, 0)
            pos_x -= 20
            self.segments.append(new_part)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            next_segment_pos = self.segments[i - 1].position()
            self.segments[i].goto(next_segment_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)