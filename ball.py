from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(2, 2)
        self.color('#1591DC')
        self.penup()
        self.x = 500
        self.y = -383
        self.dx = 5
        self.dy = 5
        self.start_x=500
        self.start_y=-383

    def bouncing_ball(self):
        self.x += self.dx
        self.y += self.dy

        if self.x > 985 or self.x < -985:
            self.dx = -self.dx
        if self.y > 785 or self.y < -785:
            self.dy = -self.dy

        self.goto(self.x, self.y)
        screen.ontimer(self.bouncing_ball, 20)

    def higher_speed(self):
      self.dx+=2
      self.dy+=2
