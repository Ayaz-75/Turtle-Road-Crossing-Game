import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.move_turtle, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_cars()
    car_manager.move_cars()

    if player.ycor() > player.finish:
        player.reset_position()
        scoreboard.refresh_score()
        car_manager.inc_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
