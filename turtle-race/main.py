import random
from turtle import Turtle, Screen

# Initialize the screen
s_obj = Screen()
s_obj.setup(500, 400)

# Ask the user to make a bet on the winning turtle color
u_bet = s_obj.textinput("Make your bet", "Which color turtle will win the race? (red, black, green, blue, brown, yellow, grey)")

# List of colors and corresponding y positions for turtles
colors = ["red", "black", "green", "blue", "brown", "yellow", "grey"]
y_index_position = [-100, -70, -40, -10, 20, 50, 80]

# Create turtles and position them on the starting line
all_turtle = []
for i in range(7):
    t_obj = Turtle(shape="turtle")
    t_obj.penup()
    t_obj.color(colors[i])
    t_obj.goto(x=-230, y=y_index_position[i])
    all_turtle.append(t_obj)

# Check if the user made a bet
if u_bet:
    race_start = True

# Start the race
while race_start:
    for turtle in all_turtle:
        # Move each turtle a random distance forward
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        # Check if any turtle has reached the finish line
        if turtle.xcor() > 220:
            race_start = False
            winning_color = turtle.pencolor()
            # Determine the winner and print the result
            if winning_color == u_bet:
                print(f"Congratulations! Your '{winning_color} turtle' won the race.")
            else:
                print(f"Unfortunately, you lose. '{winning_color} turtle' is the winner of the race.")

# Exit the screen when clicked
s_obj.exitonclick()
