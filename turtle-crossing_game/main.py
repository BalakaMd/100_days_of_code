import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player = Player()
score_board = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")
screen.setup(width=600, height=600)

game_is_on = True
count = 0
cars = CarManager()
while game_is_on:
    time.sleep(0.1)
    cars.move_car()
    screen.update()
    # Create new cars every 6 loops
    if count < 7:
        count += 1
    else:
        cars.create_car()
        count = 0
    # Detect collusion with cars
    for car in cars.list_of_cars:
        if player.distance(car) < 30:
            game_is_on = False
            score_board.game_over()
    # Detect next level
    if player.on_finish():
        cars.level_up()
        player.go_to_start()
        score_board.update_level()
screen.exitonclick()
