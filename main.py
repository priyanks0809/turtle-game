from turtle import Screen
import time
from player import Player
from car_manager import Cars
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = Cars()
score = Score()


screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 200:
        car_manager.increase_speed()
        player.reset_pos()
        score.update_level()


    car_manager.create()
    car_manager.move()

    for chosen_car in car_manager.cars:
        if player.distance(chosen_car) < 25:
            score.game_end()
            game_is_on = False

screen.exitonclick()