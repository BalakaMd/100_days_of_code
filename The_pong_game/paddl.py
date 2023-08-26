from turtle import Turtle


class Paddl(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_a_paddl()

    def create_a_paddl(self):
        self.shape('square')
        self.color("white")
        self.penup()
        self.goto(self.position)
        self.shapesize(5, 1)

    def move_up(self):
        if self.ycor() > 220:
            pass
        else:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() < -220:
            pass
        else:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
