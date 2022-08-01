from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("slate gray")
        self.score = 0

        self.update_scoreboard()

    def create_border(self):
        for _ in range(0, 48):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(5)

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 250)
        self.write(f"{self.score}", align="left")

        self.goto(-240, -240)
        self.create_border()
        self.goto(-240, 240)
        self.create_border()

    def add_point(self):
        self.score += 1

    def game_over(self):
        self.goto(-30, 0)
        self.write(f"GAME OVER", align="left")
