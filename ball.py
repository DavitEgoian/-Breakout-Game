import turtle

class Ball:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.shape('circle')
        self.t.color('red')
        self.t.penup()
        self.t.goto(0, 0)
        self.dx = 2
        self.dy = 2

    def move(self):
        x, y = self.t.xcor() + self.dx, self.t.ycor() + self.dy
        self.t.goto(x, y)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1