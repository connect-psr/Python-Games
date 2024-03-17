import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize food appearance and position
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")  # Set turtle speed to fastest
        self.refresh()  # Place food in a random position

    def refresh(self):
        # Refresh the position of the food to a random location
        random_x = random.randint(-280, 280)  # Generate random x-coordinate within the screen bounds
        random_y = random.randint(-280, 260)  # Generate random y-coordinate within the screen bounds
        self.goto(random_x, random_y)  # Move food to the random position
