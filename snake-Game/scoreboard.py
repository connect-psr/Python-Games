from turtle import Turtle

# Constants for text alignment and font
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize score and high score from saved data
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        # Set up the scoreboard appearance
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        # Update the scoreboard with current score and high score
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        # Reset the score and update the scoreboard
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")  # Save new high score to file
        self.score = 0  # Reset score
        self.update_score()

    def increase_score(self):
        # Increase the score by 1 and update the scoreboard
        self.score += 1
        self.update_score()
