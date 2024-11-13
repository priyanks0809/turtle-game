from turtle import Turtle


class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.show_level()


    def show_level(self):
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))


    def update_level(self):
        self.level += 1
        self.clear()
        self.show_level()


    def game_end(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 30, "normal"))

