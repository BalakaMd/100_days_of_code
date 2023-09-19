from turtle import Turtle, Screen
import pandas as pd
from play import Play
from timer import Timer

screen = Screen()
screen.setup(800, 500)
screen.title("U.S. State Game")
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)
data = pd.read_csv("50_states.csv")
background_turtle = Turtle()
background_turtle.shape(image)
turtle = Play()

state = [x.lower() for x in data["state"].tolist()]
x_cor = data["x"].tolist()
y_cor = data["y"].tolist()

game_is_on = True

screen.update()
timer = Timer()
guessed_list = []

while game_is_on:
    timer.start_timer()
    if timer.check_time():
        timer.clear()
        game_is_on = False
        turtle.game_over()
        break
    user_answer = screen.textinput(f"{turtle.state_count}/50 States were guessed", "Guess the state").lower()

    if user_answer == "exit":
        break
    if user_answer in state:
        guessed_list.append(user_answer)
        index = state.index(user_answer)
        turtle.draw_answer(x_cor[index], y_cor[index], state[index])
        screen.update()

not_guessed_list = []

for item in state:
    if item in guessed_list:
        pass
    else:
        not_guessed_list.append(item)

for item in not_guessed_list:
    index = state.index(item)
    turtle.color("Green")
    turtle.draw_answer(x_cor[index], y_cor[index], state[index])
    screen.update()
print(not_guessed_list)
screen.exitonclick()
