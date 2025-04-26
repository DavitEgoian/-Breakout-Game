from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard

WIDTH, HEIGHT = 800, 600
PADDLE_MOVE = 40
BRICK_ROWS = 4
BRICK_COLS = 14
COLORS = ['red', 'orange', 'yellow', 'green']

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.title('Breakout Clone')
        self.screen.bgcolor('black')
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0)

        # Create game objects
        self.paddle = Paddle(self.screen, WIDTH, HEIGHT, PADDLE_MOVE)
        self.ball = Ball()
        self.bricks = []
        self.scoreboard = Scoreboard(WIDTH, HEIGHT)
        self._create_bricks()

        # Bind controls
        self.screen.listen()
        self.screen.onkey(self.paddle.move_left, 'Left')
        self.screen.onkey(self.paddle.move_right, 'Right')

    def _create_bricks(self):
        start_x = -WIDTH/2 + 60
        start_y = HEIGHT/2 - 80
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = start_x + col * 50
                y = start_y - row * 25
                brick = Brick(x, y, COLORS[row])
                self.bricks.append(brick)

    def run(self):
        while True:
            self.screen.update()
            self.ball.move()

            # Border collisions
            if abs(self.ball.t.xcor()) > WIDTH/2 - 10:
                self.ball.bounce_x()
            if self.ball.t.ycor() > HEIGHT/2 - 10:
                self.ball.bounce_y()

            # Paddle collision
            if (self.ball.t.ycor() < -HEIGHT/2 + 60 and
                abs(self.ball.t.xcor() - self.paddle.t.xcor()) < (5 * 20)/2):
                self.ball.bounce_y()

            # Check win condition
            if all(not brick.t.isvisible() for brick in self.bricks):
                self.scoreboard.win()
                break

            # Ball falls
            if self.ball.t.ycor() < -HEIGHT/2:
                self.scoreboard.game_over()
                break

            # Brick collisions
            for brick in self.bricks:
                if brick.t.isvisible() and self.ball.t.distance(brick.t) < 35:
                    brick.hit()
                    self.ball.bounce_y()
                    self.scoreboard.add(10)
                    break

        self.screen.mainloop()

if __name__ == '__main__':
    Game().run()