from turtle import Turtle

MOVE_DISTANCE = 20  # moves 20 spaces

# the angels where the turtle's head headed:
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []  # a list that contains the parts of the snake. Each part is a turtle object
        self.create_snake()  # the method that create the snake
        self.head = self.segments[0]  # the snake's head is the 0th place at the list

    def create_snake(self):
        """Create a snake from 3 turtle object
        Starting position: x=0, y=0
        Snake length = 3
        """
        x = 0  # starting X coordinate
        for _ in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color("black")
            new_segment.penup()
            new_segment.goto(x=x, y=0)  # go to that location
            x -= 20  # decrease the x coordinate's value by the equal amount of the snake segment's size
            self.segments.append(new_segment)  # the generated segment added to the snake

    def snake_move(self):
        """Moves the snake, like the last object moves to the next position"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # start: the length of the snake;
            # stop: at 0;
            # step: -1;
            new_x = self.segments[seg_num - 1].xcor()  # gets the previous list object (turtle) x coordinate
            new_y = self.segments[seg_num - 1].ycor()  # gets the previous list object (turtle) y coordinate
            self.segments[seg_num].goto(new_x, new_y)  # the current object get the nem coordinates
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)  # go to that location
        self.segments.append(new_segment)  # the generated segment added to the snake

    def extend(self):
        """Add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def up(self):
        """If the snake not heading to down, turns up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """If the snake not heading to up, turns down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """If the snake not heading to right, turns left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """If the snake not heading to left, turns right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
