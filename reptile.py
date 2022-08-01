from turtle import Turtle


class Reptile(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("sea green")
        self.penup()
        self.setheading(90)
        self.goto(0, -270)

    def go_up(self):
        new_y = self.ycor() + 10
        if new_y < 270:
            self.goto(0, new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        if new_y > -280:
            self.goto(0, new_y)
