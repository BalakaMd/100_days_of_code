from turtle import Screen
from paddl import Paddl
from ball import Ball
from game_board import Board

screen = Screen()
screen.title("Welcome to a Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
game_is_on = True

screen.listen()

r_paddl = Paddl((350, 0))
l_paddl = Paddl((-350, 0))
ball = Ball()
board = Board()

screen.onkey(r_paddl.move_up, "Up")
screen.onkey(r_paddl.move_down, "Down")
screen.onkey(l_paddl.move_up, "w")
screen.onkey(l_paddl.move_down, "s")

while game_is_on:
    screen.update()
    ball.move()
    # Detect wall collusion
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    # Detect paddl collusion
    if ball.xcor() > 330 and ball.distance(r_paddl) < 50:
        ball.paddl_bounce()
        ball.x_cor_step -= 0.5
    if ball.xcor() < -330 and ball.distance(l_paddl) < 50:
        ball.paddl_bounce()
        ball.x_cor_step += 0.5
    # Detect user goals
    if ball.xcor() > 350:
        ball.paddl_bounce()
        ball.goto(0, 0)
        board.up_l_score()
        ball.x_cor_step = 1
    if ball.xcor() < -350:
        ball.paddl_bounce()
        ball.goto(0, 0)
        board.up_r_score()
        ball.x_cor_step = 1

screen.exitonclick()
