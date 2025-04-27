# Breakout-Game
Clone of the 80s hit game Breakout.

## 🚀 Features

- **Arcade-Style Gameplay**: Classic paddle, ball, and brick mechanics.
- **Smooth Paddle Control**: Continuous left/right movement with adjustable speed.
- **Multiple Brick Rows**: Four rows of bricks in red, orange, yellow, and green.
- **Scoring System**: Earn 10 points per brick; displays current score.
- **Win/Loss Conditions**: "YOU WIN!" on clearing all bricks; "Game Over" if the ball falls.
- **Restart Button**: On-screen ↻ icon to reset bricks, ball, paddle, and score without restarting.
- **Adaptive Ball Speed**: Slower start for a gentle introduction, then standard arcade pace.
- **Robust Collision Detection**: Accurate bounce logic for walls, paddle, and bricks.

## ⚙️ Requirements

- Python 3.6+
- Standard library `turtle` module

_No external dependencies required._

## 📦 Project Structure

```
Breakout-Game/
├── main.py         # Game loop, screen setup, controls, reset logic
├── ball.py         # Ball object: movement and bounce methods
├── paddle.py       # Paddle object: left/right movement with bounds checking
├── brick.py        # Brick object: grid placement and hit handling
└── scoreboard.py   # Score tracking and end-screen messages
```

## 🎨 Customization

- **Paddle Speed**: Adjust `PADDLE_MOVE` constant in `main.py`.
- **Ball Speed**: Modify `dx, dy` in `ball.py` constructor.
- **Brick Layout**: Change `BRICK_ROWS`, `BRICK_COLS`, or `COLORS` in `main.py`.
- **Screen Size**: Tweak `WIDTH` and `HEIGHT` constants.
- **Fonts & Styles**: Edit text and icon appearance via Turtle settings.

---

