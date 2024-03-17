import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Create player, car manager, and scoreboard objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(player.go_up, "Up")  # Move player turtle upwards when Up arrow key is pressed

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Delay for smoother animation
    screen.update()  # Update the screen

    # Create new cars and move existing cars
    car_manager.create_cars()
    car_manager.move_cars()

    # Check if player reaches the finish line (upper side of the screen)
    if player.ycor() > 285:
        player.new_level()  # Reset player position for the next level
        scoreboard.next_level()  # Increase the level in the scoreboard
        car_manager.level_up()  # Increase the speed of cars for the next level

    # Check for collisions between player and cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # Check if distance between car and player is less than a threshold
            game_is_on = False  # End the game if collision occurs
            scoreboard.game_end()  # Display "GAME OVER" in the scoreboard

# Exit the game when the screen is clicked
screen.exitonclick()
