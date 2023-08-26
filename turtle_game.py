from turtle import Turtle, Screen

tiny_turtle = Turtle()
tiny_turtle.write("Hellow", move=False, align='left', font=('Arial', 20, 'normal'))

def move_forward():
    tiny_turtle.forward(10)


def turn_left():
    tiny_turtle.left(10)


def turn_right():
    tiny_turtle.right(10)


def move_back():
    tiny_turtle.backward(10)


def clear_screen():
    tiny_turtle.clear()


screen = Screen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_back, "s")
screen.onkey(clear_screen, "c")
screen.listen()
screen.exitonclick()
