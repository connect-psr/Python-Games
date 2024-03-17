from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Set up the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off screen updates

# Create snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Listen for key events to control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause to control the speed of the game

    # Move the snake
    snake.move()

    # Detect collision with food and increase score
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh food position
        snake.extend()  # Extend the snake
        scoreboard.increase_score()  # Increase score

    # Detect collision with wall
    if (
        snake.head.xcor() > 285
        or snake.head.xcor() < -285
        or snake.head.ycor() > 285
        or snake.head.ycor() < -285
    ):
        scoreboard.reset()  # Reset score
        snake.reset()  # Reset snake position

    # Detect collision with snake's body
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()  # Reset score
            snake.reset()  # Reset snake position

# Exit the game when clicking on the screen
screen.exitonclick()
