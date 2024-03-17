import turtle
import pandas

screen = turtle.Screen()
screen.title("Bharat States Game")
screen.setup(700, 800)
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_state.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 37:
    ans_state = screen.textinput(title=f"{len(guess_states)}/36 State/UT Correct ",
                                 prompt="Enter next state name: ").title()

    if ans_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if ans_state in all_states:
        guess_states.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans_state)


screen.exitonclick()
