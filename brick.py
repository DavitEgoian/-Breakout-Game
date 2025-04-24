import turtle

class Brick:
    def __init__(self, x, y, color):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.shape('square')
        self.t.color(color)
        self.t.shapesize(stretch_wid=1, stretch_len=2)
        self.t.penup()
        self.t.goto(x, y)

    def hit(self):
        self.t.hideturtle()