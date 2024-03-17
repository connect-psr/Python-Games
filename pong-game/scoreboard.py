from turtle import Turtle

# Global constant for font style
FONT = ("Courier", 30, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize scoreboard attributes
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0  # Left player's score
        self.r_score = 0  # Right player's score
        self.update_scoreboard()

    def update_scoreboard(self):
        # Update the scoreboard with the latest scores
        self.clear()
        self.goto(-100, 250)  # Position for left player's score
        self.write(self.l_score, align="center", font=FONT)  # Write left player's score
        self.goto(100, 250)   # Position for right player's score
        self.write(self.r_score, align="center", font=FONT)  # Write right player's score

    def l_point(self):
        # Increase left player's score by 1 and update scoreboard
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        # Increase right player's score by 1 and update scoreboard
        self.r_score += 1
        self.update_scoreboard()
