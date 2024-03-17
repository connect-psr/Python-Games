from turtle import Turtle

# Define the font for the scoreboard
FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize the scoreboard
        self.color("black")
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-285, 270)
        self.display()

    def next_level(self):
        # Increase the level and update the scoreboard
        self.level += 1
        self.display()

    def display(self):
        # Clear the scoreboard and display the current level
        self.clear()
        self.write(arg=f"Level:{self.level} ", align="left", font=FONT)

    def game_end(self):
        # Display "GAME OVER" in red at the center of the screen
        self.color("red")
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 20, "bold"))
