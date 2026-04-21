def move_testudo(board, current_pos, move, jumps_left):
    """
Handles player movement and jump logic.

Args:
    board (list): game board
    current_pos (tuple): current position
    move (str): player input
    jumps_left (int): remaining jumps

Returns:
    tuple: updated position and jumps left

Author:
    Milio

Techniques:
    conditional expressions
"""

    row, col = current_pos      
    
    # Movement commands
    if move.lower() == 'w' and row > 0:
        return (row - 1, col), jumps_left

    elif move.lower() == 's' and row < len(board) - 1:
        return (row + 1, col), jumps_left

    elif move.lower() == 'a' and col > 0:
        return (row, col - 1), jumps_left

    elif move.lower() == 'd' and col < len(board[0]) - 1:
        return (row, col + 1), jumps_left
    
    elif move.lower().startswith('j'):
        if jumps_left > 0:
            parts = move.split()
            if len(parts) == 3:
                target_row = int(parts[1])
                target_col = int(parts[2])
            
            if (abs(target_row - row) <= 1 and 
                0 <= target_row < len(board) and 
                0 <= target_col < len(board[0])):
                return (target_row, target_col), jumps_left - 1
            else:
                print("Invalid jump location. Must be within one row.")
        else:
            print("Invalid jump format. Use 'j row col'")
    else:
        print("No jumps left" if jumps_left == 0 else "") 
        
       
    return current_pos, jumps_left
