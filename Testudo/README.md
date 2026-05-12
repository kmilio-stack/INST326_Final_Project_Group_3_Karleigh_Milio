# Testudo Game

## Description
This is a text-based Python game where the player controls Testudo (The UMD mascot) and attempts to safely cross a moving board to reach the goal, his exam location. The player must avoid obstacles, use jumps strategically, and make decisions each turn to survive and win.

## How the Game Works
- The player moves using WASD controls
- The board shifts each turn based on row speeds
- The player can jump using the "j row col" command
- The goal is to reach the bottom row without hitting obstacles

## Files in Repo
- board.py
- player.py
- game.py
- game1.testudo
- game2.testudo
- game3.testudo


## Attribution Table
| Method/Function | Primary Author |   Technique Claimed   |
| --------------- | -------------- | ----------------------|
| __init__()      | Karleigh Milio | 2. optional parameters|
| jump()          | Karleigh Milio | 6. sequence unpacking |
|

## Annotated Bibliography

1.
Game Loop · Sequencing Patterns · Game Programming Patterns. (2014). 
    Gameprogrammingpatterns.com. https://gameprogrammingpatterns.com/game-loop.html

We used this source to research Game Loops, which allowed us to write  the
initial set up of the game in a proper technique. This source explains how 
a game loop processes user input without blocking, updates the game state, 
and renders the game continuously, which was utilized in the game.py file.

2.
Architecture, Performance, and Games · Introduction · Game Programming Patterns. 
(n.d.). Gameprogrammingpatterns.com. https://gameprogrammingpatterns.com/architecture-performance-and-games.html

We used this source to fully understand how software architects can utilize 
python in order to build a playable game using the terminal. It also helped us 
recognize when our code was confusing, and would be difficult to update if 
it remained in that format. This source made us realize that simplicity is best, 
for our sakes while initially writing, and especially so in the debugging process. 