from turtle import Turtle

STARTING_POINT = (0, -280)
MOVE = 10
FINISH_LINE = 200


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.set_pos()


    def set_pos(self):
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POINT)


    def move(self):
        self.forward(MOVE)


    def reset_pos(self):
        self.set_pos()
