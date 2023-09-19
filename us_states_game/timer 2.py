from datetime import datetime, timedelta
from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Timer(Turtle):

    def __init__(self):
        super().__init__()
        self.time_now = None
        self.timer = None
        self.timer_str = None
        self.hideturtle()
        self.ten_minutes = datetime.now() + timedelta(minutes=10)
        self.goto(150, 250)
        self.start_timer()

    def start_timer(self):
        self.clear()
        self.time_now = datetime.now()
        self.timer = self.ten_minutes - self.time_now
        self.timer_str = f"{str(self.timer)[2:7]}"
        self.write(f"Time left:{self.timer_str}", font=FONT)

    def check_time(self):
        if self.timer_str == " day,":
            return True

