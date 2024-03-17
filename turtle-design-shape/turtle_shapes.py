from turtle import Turtle, Screen

# Define a list of colors
color_list = ["yellow", "black", "pink", "blue", "grey", "green", "red"]

# Initialize the number of sides for the first polygon
n = 3

# Create a Turtle object
turtle_obj1 = Turtle()

# Loop through each color in the color list
for i in range(7):
    # Draw a polygon with the current color
    for _ in range(n):
        turtle_obj1.forward(100)  # Move the turtle forward by 100 units
        turtle_obj1.right(360/n)  # Turn the turtle to the right by the angle calculated based on the number of sides
        turtle_obj1.color(color_list[i])  # Set the color of the turtle to the current color
    n += 1  # Increment the number of sides for the next polygon

# Create a Screen object
screen_obj = Screen()

# Exit the program when the screen is clicked
screen_obj.exitonclick()
