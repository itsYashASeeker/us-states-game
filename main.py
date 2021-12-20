import pandas
import turtle

screen = turtle.Screen()
screen.title("Quiz-Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
state_lists = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer = screen.textinput(f"{len(guessed_state)}/50 CORRECT!!", "Guess The State Name!").title()
    if answer == "Exit":
        missing_states = []
        for states in state_lists:
            if states not in guessed_state:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to learn.csv")
        break
    for state_name in state_lists:
        if state_name == answer:
            guessed_state.append(answer)
            tu = turtle.Turtle()
            tu.hideturtle()
            tu.penup()
            state_data = data[data.state == answer]
            tu.goto(int(state_data.x), int(state_data.y))
            tu.write(state_data.state.item())