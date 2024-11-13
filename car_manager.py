from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOV_DIST = 5
MOV_DIST = 5


class Cars:

    def __init__(self):
        self.cars = []
        self.create()
        self.car_speed = STARTING_MOV_DIST

    def create(self):
        rand_choice = random.randint(1, 6)
        if rand_choice == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            set_y = random.randint(-200, 180)
            car.goto(300, set_y)
            self.cars.append(car)


    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)


    def increase_speed(self):
        self.car_speed += MOV_DIST
