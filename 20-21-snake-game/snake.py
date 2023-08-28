from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180



# Create the snake body
class Snake:
    def __init__(self):
        self.segments = []
        self.__create_snake()
        self.head = self.segments[0]

    def __create_snake(self):
        for position in STARTING_POSITION:
            self.__add_segment(position)

    def __add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        last_segment_pos = self.segments[-1].position()
        self.__add_segment(last_segment_pos)

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

