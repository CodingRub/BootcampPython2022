import turtle, pandas


screen = turtle.Screen()
screen.title("US States Game")
img = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/us-states-game/blank_states_img.gif"
csv = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/us-states-game/50_states.csv"
screen.addshape(img)
turtle.shape(img)
data = pandas.read_csv(csv)
all_states = data.state.to_list()
guessed_states = []

running = True
while len(guessed_states) <= 50 and running:
    answer_state = screen.textinput(f"{len(guessed_states)}/{len(all_states)} States Correct", "What's another state's name ?").title()
    if answer_state in all_states:
        if answer_state not in guessed_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
            guessed_states.append(state_data.state.item())
    elif answer_state == None:
        running = False
    elif answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

screen.exitonclick()
