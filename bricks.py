from turtle import Turtle

class Bricks(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color('#B331F1')
        self.penup()
        self.goto(x, y)

def creating_bricks():
    bricks = []
    for row in range(5):
        for col in range(10):
            x = -200 + col * 45
            y = 230 + row * 25
            brick = Bricks(x, y)
            bricks.append(brick)
    return bricks
