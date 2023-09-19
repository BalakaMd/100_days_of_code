from turtle import Screen
from snake import Snake
from Food import Food
from game_board import Score, draw_game_boards
import time

screen = Screen()
screen.title("Welcome to a Snake Game")
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.tracer(0)


def game():
    snake = Snake()
    food = Food()
    game_board = Score()
    screen.listen()
    draw_game_boards()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    game_is_on = True

    while game_is_on:
        screen.update()
        # time.sleep(0.05)
        snake.move_forward()

        # Detect collusion in food
        if snake.head.distance(food) < 20:
            food.refresh()
            snake.extend()
            game_board.add_point()

        # Detect collusion in wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or \
                snake.head.ycor() > 280 or snake.head.ycor() < -290:
            game_is_on = False
            if game_board.score > game_board.high_score:
                game_board.high_score = game_board.score
            game_board.game_over()
            game_board.save_h_score()
        # Detect collusion in tail
        for segment in snake.segments_list[1:]:
            if snake.head.distance(segment) < 3:
                game_is_on = False
                game_board.game_over()


game()


def restart_game():
    screen.reset()
    game()


screen.onkey(restart_game, "space")
screen.exitonclick()
