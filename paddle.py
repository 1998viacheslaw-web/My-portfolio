from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(1,5,2)
        self.color("#B331F1")
        self.penup()
        self.goto(0, -390)

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)
