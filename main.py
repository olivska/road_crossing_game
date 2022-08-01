from turtle import Screen
from reptile import Reptile
from scoreboard import Scoreboard
from car import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Capstone")

screen.tracer(0)
tim = Reptile()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkeypress(tim.go_up, "Up")
screen.onkeypress(tim.go_down, "Down")

car_spacing = 10
all_cars = []

game_on = True
while game_on:
    screen.tracer(0)

    if car_spacing % 10 == 0:
        car = Car()
        car.move_to_start()
        all_cars.append(car)

    car_spacing += 1

    screen.tracer(1)

    for vehicle in all_cars:
        vehicle.drive()

        if vehicle.xcor() in range(-30, 30):
            if tim.distance(vehicle) < 25:
                game_on = False
                scoreboard.game_over()

        elif tim.distance(vehicle) < 40:
            game_on = False
            scoreboard.game_over()

        if vehicle.xcor() < -350:
            all_cars.remove(vehicle)

    if tim.ycor() > 240:
        tim.goto(0, -270)
        scoreboard.add_point()
        screen.tracer(0)
        scoreboard.update_scoreboard()
        screen.tracer(1)
        for ball in all_cars:
            time.sleep(ball.move_speed)

screen.exitonclick()
