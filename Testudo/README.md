# Testudo Game

## Description
This is a text-based Python game where the player controls Testudo (The UMD mascot) and attempts to safely cross a moving board to reach the goal, his exam location. The player must avoid obstacles, use jumps strategically, and make decisions each turn to survive and win.

## How the Game Works
- The player moves using WASD controls when prompted in the terminal
- The board shifts each turn based on row speeds
- The player can jump using the "j row col" command
- The goal is to reach the bottom row without hitting obstacles

## Understanding Game Board Display
- Each turn, the game prints the board and the current turn number:
Turn 1
- The board contains:
    - 🐢 (Testudo) = the player
    - _ = empty safe space
    - moving obstacle characters = dangerous spaces
    - the top row = starting safe row
    - the bottom row = winning safe row
    - The player begins in the top safe row and must move downward to reach 
the bottom safe row.

## How To Run Game From Command Line

- Open terminal
- Navigiate to the folder files are saved to using "cd~/...."
- Once inside correct folder, type "python3 game.py"
- When available .testudo game files are returned in the terminal, the user can choose which level using 1, 2, or 3, depending on difficulty they want to play.
- The game then asks for user move input, "WASD or j row col >>"
- User inputs location they want to move to for their turn, using WASD, 
or they can choose to use 1 jump by typing "j row col" in terminal, where desired 
row and column numbers would replace "row" and "col"
- Example of full gameplay terminal inputs: 

    cd ~/INST326_Final_Project_Group_3_Karleigh_Milio/Testudo

    python3 game.py

    1
    d
    d
    s
    j 3 4
    w



## How To Use Program

- 

## Files in Repo
- board.py (used for creating the game board, controlling the movement of obstacles)
- player.py
- game.py
- game1.testudo
- game2.testudo
- game3.testudo
- README.md



## Attribution Table
| Method/Function | Primary Author |   Technique Claimed   |
| --------------- | -------------- | ----------------------|
|    __init__()   | Karleigh Milio | 2. optional parameters|
|     jump()      | Karleigh Milio | 6. sequence unpacking |
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