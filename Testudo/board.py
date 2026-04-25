# Constants
TESTUDO = '\U0001F422'
EMPTY_SPACE = '_'
SAFE = ' '
def rotate_board(board, speeds):
    """
    Rotates each row of the board based on it speed.
    
    Args:
        board (list): 2D list representing the game board.
        speeds (list): movement speed per row.
    
    Returns:
        list: rotated board
    
    Author:
        Brevard
    
    """
    rotated_board = []
    for i in range(len(board)):
        row = board[i]
        speed = speeds[i] % len(row)
        rotated_row = row[-speed:] + row[:-speed]
        rotated_board.append(rotated_row)
    
    return rotated_board

def check_collision(board, testudo_pos):
    """
    Checks if the player has collided with an obstacle.
    
    Args:
        board (list): 2D game board
        testudo_pos (tuple): (row, col) position
    
    Returns:
        bool: True if a collision occurs otherwise false.
    
    Author:
        Brevard
    """
    row, col = testudo_pos
    return board[row][col] != EMPTY_SPACE and board[row][col] != SAFE

def display_board(board, testudo_pos, jumps_left):
    """
    Displays the board with the player position
    
    Args:
        board (list): 2D game board
        testudo_pos (tuple): player position
        jumps_left (int): remaining jumps
    
    Returns:
        None
    
    Author:
        Brevard
    """
    temp_board = []
    for row in board:
        new_row = []
        for item in row:
            new_row.append(item)
        temp_board.append(new_row)
    
    testudo_row, testudo_col = testudo_pos
    temp_board[testudo_row][testudo_col] = TESTUDO
    
    print(" ", end= " ")
    for i in range(len(board[0])):
        print(f"{i:2}", end="")
    print()
    
    row_index = 0
    for row in temp_board:
        print(f"{row_index:2}", end=" ")
        print("".join(row))
        row_index +=1
        
    print(f"Jumps left: {jumps_left}")