import turtle
from turtle import Turtle, Screen
import random

# Create a Turtle object
turtleObj = Turtle()

# Set the shape of the turtle to a triangle
turtleObj.shape("triangle")

# Set the color mode to use RGB values
turtle.colormode(255)

# Define a list of directions (angles) for the turtle to choose from
direction_list = [0, 90, 180, 270]

# Set the pen size to 10
turtleObj.pensize(10)

# Function to generate a random color
def random_color():
    r = random.randint(0, 255)  # Generate a random value for red (R)
    g = random.randint(0, 255)  # Generate a random value for green (G)
    b = random.randint(0, 255)  # Generate a random value for blue (B)
    random_color_tuple = (r, g, b)  # Create a tuple with the RGB values
    return random_color_tuple  # Return the random color tuple

# Loop to draw 100 lines
for _ in range(100):
    turtleObj.color(random_color())  # Set the color of the turtle to a random color
    turtleObj.forward(30)  # Move the turtle forward by 30 units
    turtleObj.setheading(random.choice(direction_list))  # Set the turtle's heading to a random direction

# Create a Screen object
screenObj = Screen()

# Exit the program when the screen is clicked
screenObj.exitonclick()
