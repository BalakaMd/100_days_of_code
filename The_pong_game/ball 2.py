from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color("white")
        self.x_cor_step = 3
        self.y_cor_step = 3

    def move(self):
        new_x = self.xcor() + self.x_cor_step
        new_y = self.ycor() + self.y_cor_step
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_cor_step *= -1

    def paddl_bounce(self):
        self.x_cor_step *= -1
