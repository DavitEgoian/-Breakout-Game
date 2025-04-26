import turtle

class Paddle:
    def __init__(self, screen, width, height, move_distance):
        self.move_distance = move_distance
        self.screen_width = width
        # Create paddle
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.shape('square')
        self.t.color('white')
        self.t.shapesize(stretch_wid=1, stretch_len=5)
        self.t.penup()
        start_y = -height/2 + 50
        self.t.goto(0, start_y)

    def move_left(self):
        new_x = self.t.xcor() - self.move_distance
        half_paddle = (5 * 20) / 2
        left_limit = -self.screen_width/2 + half_paddle
        if new_x < left_limit:
            new_x = left_limit
        self.t.goto(new_x, self.t.ycor())

    def move_right(self):
        new_x = self.t.xcor() + self.move_distance
        half_paddle = (5 * 20) / 2
        right_limit = self.screen_width/2 - half_paddle
        if new_x > right_limit:
            new_x = right_limit
        self.t.goto(new_x, self.t.ycor())