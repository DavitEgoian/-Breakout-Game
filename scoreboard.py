import turtle

class Scoreboard:
    def __init__(self, width, height):
        self.score = 0
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color('white')
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, height/2 - 40)
        self.update()

    def update(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}", align='center', font=('Courier', 24, 'normal'))

    def add(self, points):
        self.score += points
        self.update()

    def game_over(self):
        self.pen.clear()
        self.pen.goto(0, 0)
        self.pen.write("Game Over", align='center', font=('Courier', 36, 'normal'))

    def win(self):
        self.pen.clear()
        self.pen.goto(0, 0)
        self.pen.write("YOU WIN!", align='center', font=('Courier', 36, 'normal'))