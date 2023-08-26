from turtle import Turtle, Screen
from random import choice

tiny_turtle = Turtle()
tiny_turtle.shape("turtle")
tiny_turtle.color('green')
n_angels = 3
tiny_turtle.speed(0)
angle = 0

for _ in range(37):
    tiny_turtle.circle(100, steps=100)
    tiny_turtle.setheading(angle)
    angle += 10

screen = Screen()
screen.exitonclick()
