import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian State Games")
image = "blank_states_img.gif"
screen.setup(width=500, height=500)
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)

# # For getting the coordinates of all the states on map
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessed_state = []

while len(guessed_state) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/29 Guess the State",
                                    prompt="Which state ??").title()
    data = pandas.read_csv("29_states.csv")
    states = data.state.to_list()
    if answer_state == "Exit":
        break
    if answer_state in states and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinates = data[data.state == answer_state]
        t.goto(int(coordinates.x), int(coordinates.y))
        t.write(answer_state)

# states to learn.csv
missed_states = []
for _ in states:
    if _ not in guessed_state:
        missed_states.append(_)
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("states_to_learn.csv")


screen.exitonclick()