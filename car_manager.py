import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.all_cars = []
        self.make_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            cars = Turtle("square")
            cars.penup()
            cars.shapesize(stretch_wid=1, stretch_len=2)
            cars.color(random.choice(COLORS))
            random_y = random.randint(-240, 240)
            cars.goto(300, random_y)
            self.all_cars.append(cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def inc_speed(self):
        self.car_speed += MOVE_INCREMENT

