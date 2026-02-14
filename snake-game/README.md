# Terminal Snake Game 🐍

A classic Snake game that runs in your terminal, written in Python using the `curses` library.

## How to Play

1. Run the game:
   ```bash
   python snake.py
   ```

2. Controls:
   - **Arrow Keys** or **WASD** - Move the snake
   - **Q** - Quit the game

3. Objective:
   - Eat the food (`*`) to grow and score points
   - Avoid hitting the walls or yourself
   - The game speeds up as your score increases!

## Requirements

- Python 3.x
- A terminal that supports curses (most Unix/Linux/macOS terminals)
- For Windows, you may need to install `windows-curses`:
  ```bash
  pip install windows-curses
  ```

## Game Elements

- `#` - Snake head
- `o` - Snake body
- `*` - Food

## Scoring

- Each food eaten: +10 points
- Game speeds up every 20 points

Enjoy the game!
