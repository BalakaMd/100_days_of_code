from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-220, 260)
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write("Game Over", font=FONT)
