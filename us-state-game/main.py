import turtle
import pandas

ALIGN = "center"
FONT = ("courier", 8, "normal")
image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
attempt = 0
correct_states = []
guessed_states = []
state_no = "State"

game_on = True
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 {state_no} Correct",
                                    prompt="What's another state name").title()
    if answer_state == "Exit":
        break
    guessed_states.append(answer_state)
    if answer_state in state_list:
        correct_states.append(answer_state)
        state_write = turtle.Turtle()
        state_write.hideturtle()
        state_write.penup()
        answer_row = data[data.state == answer_state]
        x = int(answer_row.x.iloc[0])
        y = int(answer_row.y.iloc[0])
        state_write.goto(x, y)
        state_write.write(f"{answer_state}", align=ALIGN, font=FONT)

not_guessed = [state for state in state_list if state not in correct_states]
data_csv = pandas.DataFrame(not_guessed)
data_csv.to_csv("Answer_not_guessed.csv")


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
