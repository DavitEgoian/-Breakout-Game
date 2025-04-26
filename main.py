from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import tkinter as tk

WIDTH, HEIGHT = 800, 600
PADDLE_MOVE = 5  # Reduced move distance for smoother motion
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

        # Game state
        self.game_active = True
        self.moving_left = False
        self.moving_right = False

        # Create game objects
        self.paddle = Paddle(self.screen, WIDTH, HEIGHT, PADDLE_MOVE)
        self.ball = Ball()
        self.bricks = []
        self.scoreboard = Scoreboard(WIDTH, HEIGHT)
        self._create_bricks()

        # Bind controls with press/release events
        self.screen.listen()
        self.screen.onkeypress(self.start_moving_left, 'Left')
        self.screen.onkeyrelease(self.stop_moving_left, 'Left')
        self.screen.onkeypress(self.start_moving_right, 'Right')
        self.screen.onkeyrelease(self.stop_moving_right, 'Right')

        # Add restart icon
        canvas = self.screen.getcanvas()
        root = canvas.winfo_toplevel()
        self.restart_button = tk.Button(
            root, text="↻", command=self.reset,
            font=('Arial', 14, 'bold'), width=2, height=1
        )
        self.restart_button.pack(side='bottom')

    def start_moving_left(self):
        if self.game_active:
            self.moving_left = True

    def stop_moving_left(self):
        self.moving_left = False

    def start_moving_right(self):
        if self.game_active:
            self.moving_right = True

    def stop_moving_right(self):
        self.moving_right = False

    def _create_bricks(self):
        start_x = -WIDTH/2 + 60
        start_y = HEIGHT/2 - 80
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = start_x + col * 50
                y = start_y - row * 25
                brick = Brick(x, y, COLORS[row])
                self.bricks.append(brick)

    def reset(self):
        # Reset game state
        self.moving_left = False
        self.moving_right = False
        for brick in self.bricks:
            brick.t.hideturtle()
        self.bricks.clear()
        self._create_bricks()
        self.ball.t.goto(0, 0)
        self.ball.dx, self.ball.dy = 2, 2
        self.paddle.t.goto(0, -HEIGHT/2 + 50)
        self.scoreboard.score = 0
        self.scoreboard.update()
        self.game_active = True

    def run(self):
        while True:
            self.screen.update()
            if self.game_active:
                # Handle continuous paddle movement
                if self.moving_left:
                    self.paddle.move_left()
                if self.moving_right:
                    self.paddle.move_right()

                self.ball.move()

                # Border collisions
                if abs(self.ball.t.xcor()) > WIDTH/2 - 10:
                    self.ball.bounce_x()
                if self.ball.t.ycor() > HEIGHT/2 - 10:
                    self.ball.bounce_y()

                # Paddle collision
                paddle_half_width = (5 * 20) / 2 - 8
                if (self.ball.t.ycor() < -HEIGHT / 2 + 60 and
                        abs(self.ball.t.xcor() - self.paddle.t.xcor()) < paddle_half_width):
                    self.ball.bounce_y()
                # Win condition
                if all(not brick.t.isvisible() for brick in self.bricks):
                    self.scoreboard.win()
                    self.game_active = False

                # Ball falls
                if self.ball.t.ycor() < -HEIGHT/2:
                    self.scoreboard.game_over()
                    self.game_active = False

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