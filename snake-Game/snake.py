from turtle import Turtle

# Constants for snake starting positions, movement distance, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        # Initialize snake segments and create the initial snake
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Set the head of the snake

    def create_snake(self):
        # Create the initial segments of the snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Add a new segment to the snake
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def reset(self):
        # Reset the snake to its initial state
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move segments off screen
        self.segments.clear()  # Clear segments list
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]  # Set the head of the snake

    def extend(self):
        # Extend the length of the snake by adding a new segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake forward
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Change the snake's direction to up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the snake's direction to down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # Change the snake's direction to right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        # Change the snake's direction to left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
