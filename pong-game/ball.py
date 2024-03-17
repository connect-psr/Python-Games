from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # Ball appearance and initial position
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(0, 0)
        # Ball movement attributes
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1  # Initial speed

    def move(self):
        # Move the ball
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Change ball's y direction upon collision with the wall
        self.y_move *= -1

    def bounce_x(self):
        # Change ball's x direction upon collision with a paddle
        self.x_move *= -1
        # Increase speed after each paddle collision
        self.ball_speed *= 0.9

    def reset_position(self):
        # Reset ball position to the center
        self.goto(0, 0)
        # Reset ball speed and direction
        self.ball_speed = 0.1
        self.bounce_x()
