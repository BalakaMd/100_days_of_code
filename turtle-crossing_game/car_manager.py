from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.list_of_cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape('square')
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.goto(280, random.randint(-200, 250))
        self.list_of_cars.append(new_car)

    def move_car(self):
        for car in self.list_of_cars:
            pos_x = car.xcor() - self.car_speed
            pos_y = car.ycor()
            car.goto(pos_x, pos_y)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
