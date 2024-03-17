# Importing necessary modules and classes
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Setting up the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Creating right and left paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

# Listening to keyboard events
screen.listen()
screen.onkey(r_paddle.go_up, "Up")       # Move right paddle up
screen.onkey(r_paddle.go_down, "Down")   # Move right paddle down
screen.onkey(l_paddle.go_up, "w")         # Move left paddle up
screen.onkey(l_paddle.go_down, "x")     # Move left paddle down

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)  # Slowing down the ball movement
    screen.update()              # Updating the screen
    ball.move()                  # Moving the ball

    # ------- Detect collision with wall -------- #
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()          # Change ball's y direction

    # ------- Detect collision with paddle -------- #
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()          # Change ball's x direction

    # ------- Detect ball miss r_paddle -------- #
    if ball.xcor() > 380:
        ball.reset_position()    # Reset ball position
        scoreboard.l_point()     # Increase left paddle's score

    # ------- Detect ball miss l_paddle -------- #
    if ball.xcor() < -380:
        ball.reset_position()    # Reset ball position
        scoreboard.r_point()     # Increase right paddle's score

# Exit the game when clicking on the screen
screen.exitonclick()
