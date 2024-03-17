from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # Paddle appearance and initial position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        # Move paddle upwards
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # Move paddle downwards
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
