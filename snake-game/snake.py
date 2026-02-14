#!/usr/bin/env python3
"""
Simple Snake Game for Terminal
Use arrow keys or WASD to control the snake.
Press 'q' to quit.
"""

import curses
import random
import time


def main(stdscr):
    # Setup curses
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh rate (ms) - controls game speed
    
    # Get screen dimensions
    sh, sw = stdscr.getmaxyx()
    
    # Create game window
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)
    win.timeout(100)
    
    # Initial snake position (middle of screen)
    snake_y = sh // 2
    snake_x = sw // 4
    
    # Snake body (list of [y, x] coordinates)
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    
    # Initial food position
    food = [sh // 2, sw // 2]
    win.addch(food[0], food[1], '*')
    
    # Initial direction (moving right)
    direction = curses.KEY_RIGHT
    
    # Score
    score = 0
    
    # Direction mappings (including WASD)
    key_map = {
        ord('w'): curses.KEY_UP,
        ord('W'): curses.KEY_UP,
        ord('s'): curses.KEY_DOWN,
        ord('S'): curses.KEY_DOWN,
        ord('a'): curses.KEY_LEFT,
        ord('A'): curses.KEY_LEFT,
        ord('d'): curses.KEY_RIGHT,
        ord('D'): curses.KEY_RIGHT,
    }
    
    # Opposite directions (to prevent 180-degree turns)
    opposite = {
        curses.KEY_UP: curses.KEY_DOWN,
        curses.KEY_DOWN: curses.KEY_UP,
        curses.KEY_LEFT: curses.KEY_RIGHT,
        curses.KEY_RIGHT: curses.KEY_LEFT,
    }
    
    while True:
        # Display score
        win.addstr(0, 2, f' Score: {score} ')
        win.addstr(0, sw - 20, ' Press Q to quit ')
        
        # Get user input
        key = win.getch()
        
        # Quit game
        if key in [ord('q'), ord('Q')]:
            break
        
        # Map WASD to arrow keys
        if key in key_map:
            key = key_map[key]
        
        # Change direction (prevent 180-degree turns)
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if key != opposite.get(direction):
                direction = key
        
        # Calculate new head position
        head = snake[0].copy()
        
        if direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            head[1] += 1
        
        # Check for collisions with walls
        if head[0] <= 0 or head[0] >= sh - 1 or head[1] <= 0 or head[1] >= sw - 1:
            break
        
        # Check for collision with self
        if head in snake:
            break
        
        # Insert new head
        snake.insert(0, head)
        
        # Check if snake ate food
        if head == food:
            score += 10
            # Generate new food position
            while True:
                food = [
                    random.randint(2, sh - 2),
                    random.randint(2, sw - 2)
                ]
                if food not in snake:
                    break
            win.addch(food[0], food[1], '*')
            # Increase speed slightly
            new_timeout = max(50, 100 - score // 2)
            win.timeout(new_timeout)
        else:
            # Remove tail (snake doesn't grow)
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')
        
        # Draw snake head
        win.addch(snake[0][0], snake[0][1], '#')
        
        # Draw snake body
        for segment in snake[1:]:
            win.addch(segment[0], segment[1], 'o')
    
    # Game Over screen
    win.clear()
    game_over_msg = "GAME OVER!"
    score_msg = f"Final Score: {score}"
    exit_msg = "Press any key to exit..."
    
    win.addstr(sh // 2 - 1, sw // 2 - len(game_over_msg) // 2, game_over_msg)
    win.addstr(sh // 2, sw // 2 - len(score_msg) // 2, score_msg)
    win.addstr(sh // 2 + 2, sw // 2 - len(exit_msg) // 2, exit_msg)
    
    win.nodelay(0)
    win.getch()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
        print("Thanks for playing Snake!")
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
