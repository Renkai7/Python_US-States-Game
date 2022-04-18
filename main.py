import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read data from csv
data = pandas.read_csv("50_states.csv")

# Get list of states
states_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Convert guess to Title case
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state_name in states_list:
            if state_name not in guessed_states:
                missing_states.append(state_name)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)
    elif answer_state in guessed_states:
        print(f"You've already guessed {answer_state}")


screen.exitonclick()
