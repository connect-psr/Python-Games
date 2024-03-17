from turtle import Turtle

# Define constants for starting position, movement distance, and finish line
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize the player attributes
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)  # Face the turtle upwards
        self.goto(STARTING_POSITION)  # Position the turtle at the starting position

    def go_up(self):
        # Move the player turtle upwards
        self.forward(MOVE_DISTANCE)

    def new_level(self):
        # Reset the player turtle to the starting position for a new level
        self.goto(STARTING_POSITION)
