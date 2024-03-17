from turtle import Turtle
import random

# Define constants for colors, starting move distance, and move increment
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        # Initialize car manager attributes
        self.all_cars = []  # List to store all car turtles
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars

    def create_cars(self):
        # Create new cars randomly
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # Adjust the probability of creating a new car
            new_car = Turtle("square")  # Create a new car turtle
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Set the size of the car
            new_car.penup()  # Lift the pen to avoid drawing lines
            new_car.color(random.choice(COLORS))  # Choose a random color for the car
            random_y = random.randint(-250, 250)  # Choose a random y-coordinate for the car
            new_car.goto(300, random_y)  # Position the car off-screen on the right side
            self.all_cars.append(new_car)  # Add the new car to the list of all cars

    def move_cars(self):
        # Move all cars towards the left
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move the car backward (to the left)

    def level_up(self):
        # Increase the speed of cars when the player advances to the next level
        self.car_speed += MOVE_INCREMENT  # Increase the car speed by the move increment
