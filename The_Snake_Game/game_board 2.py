from turtle import Turtle

ALIGN = 'center'
FONT = ('courier', 24, 'normal')


def read_h_score():
    with open("data.txt", mode="r") as f:
        return int(f.read())


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_h_score()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.print_score()

    def print_score(self):
        """Show current score at the top of the game board"""
        self.write(f"Score: {self.score}. High score:{self.high_score}.",
                   move=False, align=ALIGN, font=FONT)

    def game_over(self):
        """Print 'Game over'"""
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align=ALIGN, font=FONT)

    def add_point(self):
        """Increase point to 1"""
        self.clear()
        self.score += 1
        self.print_score()

    def save_h_score(self):
        with open("data.txt", mode="w") as f:
            f.write(f"{self.high_score}")


def draw_game_boards():
    """Drawing a game board"""
    board = Turtle()
    board.hideturtle()
    board.penup()
    board.pensize(10)
    board.color('white')
    board.goto(-295, 0)
    board.pendown()
    board.goto(-295, 295)
    board.goto(295, 295)
    board.goto(295, -295)
    board.goto(-295, -295)
    board.goto(-295, 0)
