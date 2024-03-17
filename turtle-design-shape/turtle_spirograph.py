import turtle
from turtle import Turtle, Screen
import random

# Create a Turtle object
turtle_Object = Turtle()

# Set the shape of the turtle to a triangle
turtle_Object.shape("triangle")

# Set the color mode to use RGB values
turtle.colormode(255)

# Set the speed of the turtle to the fastest
turtle_Object.speed("fastest")

# Function to generate a random color
def random_color():
    r = random.randint(0, 255)  # Generate a random value for red (R)
    g = random.randint(0, 255)  # Generate a random value for green (G)
    b = random.randint(0, 255)  # Generate a random value for blue (B)
    color_tuple = (r, g, b)  # Create a tuple with the RGB values
    return color_tuple  # Return the random color tuple

# Function to draw the spirograph pattern
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle_Object.color(random_color())  # Set the color of the turtle to a random color
        turtle_Object.circle(100)  # Draw a circle with a radius of 100
        current_heading = turtle_Object.heading()  # Get the current heading of the turtle
        turtle_Object.setheading(current_heading + size_of_gap)  # Update the heading by the specified gap size

# Call the draw_spirograph function with a gap size of 5 degrees
draw_spirograph(5)

# Create a Screen object
screenObj = Screen()

# Set the background color of the screen to black
screenObj.bgcolor("black")

# Exit the program when the screen is clicked
screenObj.exitonclick()
