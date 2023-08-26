from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Play(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.state_count = 0

    def draw_answer(self, x_cor, y_cor, state):
        self.state_count += 1
        self.goto(x_cor, y_cor)
        self.write(state.upper(), font=FONT, align="center")

    def game_over(self):
        self.goto(-50, 250)
        self.write("Game over!", font=("Courier", 30, "normal"))
