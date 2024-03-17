import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("Bharat States Game")
screen.setup(700, 800)

# Add the map image as a shape
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

# Read the data containing state information
data = pandas.read_csv("50_state.csv")
all_states = data.state.to_list()
guess_states = []

# Main game loop
while len(guess_states) < 37:  # Allow up to 36 correct guesses
    # Prompt the user to guess the next state
    ans_state = screen.textinput(title=f"{len(guess_states)}/36 States/UT Correct",
                                 prompt="Enter the name of the next state: ").title()

    # If the user wants to exit the game, save the states to learn and break out of the loop
    if ans_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    # Check if the guessed state is correct
    if ans_state in all_states:
        guess_states.append(ans_state)
        # Write the correct state name on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans_state)

# Exit the program when the screen is clicked
screen.exitonclick()
