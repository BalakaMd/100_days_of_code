from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()
        self.draw_game_board()

    def update_score(self):
        self.clear()
        self.draw_game_board()
        self.goto(-100, 220)
        self.write(self.l_score, align='center', font=('Courier', 80, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align='center', font=('Courier', 80, "normal"))

    def up_l_score(self):
        self.l_score += 1
        self.update_score()

    def up_r_score(self):
        self.r_score += 1
        self.update_score()

    def draw_game_board(self):
        self.goto(0, 300)
        self.pendown()
        self.setheading(270)
        for _ in range(9):
            self.forward(35)
            self.penup()
            self.forward(35)
            self.pendown()
        self.penup()
        self.pensize(10)
        self.goto(-380, 297)
        self.pendown()
        self.goto(380, 297)
        self.penup()
        self.goto(-380, -290)
        self.pendown()
        self.goto(380, -290)
        self.penup()





