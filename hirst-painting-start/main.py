import random
import turtle
from turtle import Turtle, Screen

# Set color mode to RGB
turtle.colormode(255)

# Create a Turtle object
turtle_obj1 = Turtle()

# List of colors for dots
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), 
              (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), 
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), 
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), 
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), 
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# Set turtle speed to fastest
turtle_obj1.speed("fastest")

# Set initial position and orientation of turtle_obj1
turtle_obj1.setheading(225)
turtle_obj1.hideturtle()
turtle_obj1.penup()
turtle_obj1.forward(300)
turtle_obj1.setheading(0)

# Number of dots to draw
number_of_dots = 100

# Loop to draw dots
for dot_count in range(1, number_of_dots + 1):
    turtle_obj1.dot(20, random.choice(color_list))  # Draw a dot with random color
    turtle_obj1.penup()
    turtle_obj1.forward(50)

    # Move to the next row after drawing 10 dots
    if dot_count % 10 == 0:
        turtle_obj1.setheading(90)
        turtle_obj1.forward(50)
        turtle_obj1.setheading(180)
        turtle_obj1.forward(500)
        turtle_obj1.setheading(0)

# Create a Screen object
screen_Obj = Screen()

# Exit the program when the screen is clicked
screen_Obj.exitonclick()
