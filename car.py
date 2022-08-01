import random
from turtle import Turtle


class Car(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color("crimson")
        self.penup()
        self.move_speed = 0.1

    def move_to_start(self):
        start_x = 320
        start_y = random.randint(-220, 220)
        self.goto(start_x, start_y)

    def drive(self):
        self.forward(5)

    def keep_driving(self):
        if self.xcor() < -320:
            self.move_to_start()
            self.drive()

    def speed_up(self):
        self.move_speed *= 0.9
