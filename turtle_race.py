from turtle import Turtle, Screen
import random

screen = Screen()
game_continue = True
screen.setup(width=500, height=400)
colors = ['red', 'yellow', 'green', 'blue', 'purple']
location_y = -130
tiny_list = []
user_name_list = []
user_bet_list = []

number_of_players = int(screen.numinput(title="Welcome",
                                        prompt="How many players in the game?(5 max):"))
for number in range(number_of_players):
    u_name = screen.textinput(title="Who play?",
                              prompt=f"Player {number + 1}, enter your name")
    user_name_list.append(u_name)
for color in colors:
    tiny = Turtle(shape='turtle')
    tiny.penup()
    tiny.color(f'{color}')
    tiny.goto(-200, location_y)
    location_y += 60
    tiny_list.append(tiny)

for user in user_name_list:
    user_bet = screen.textinput(title="Insert your bet",
                                prompt=f"{user}, which turtle will win the game ? Enter a color:")
    user_bet_list.append(user_bet.lower())
while game_continue:
    for tiny in tiny_list:
        step = random.randint(0, 11)
        tiny.forward(step)
        if tiny.xcor() > 230:
            winner_color = tiny.pencolor()
            game_continue = False
            if winner_color in user_bet_list:
                index_of_winner = user_bet_list.index(f"{winner_color}")
                text = f"{user_name_list[index_of_winner]} You win !"
                tiny.goto(-100, 100)
                tiny.write(text, move=False, align='left', font=('Arial', 20, 'normal'))
            else:
                tiny.goto(-100, 100)
                tiny.write("Sorry, you lost!", move=False, align='left', font=('Arial', 20, 'normal'))
            text = f"The winner is {winner_color} turtle"
            tiny.goto(-100, 150)
            tiny.write(text, move=False, align='left', font=('Arial', 20, 'normal'))
screen.exitonclick()
