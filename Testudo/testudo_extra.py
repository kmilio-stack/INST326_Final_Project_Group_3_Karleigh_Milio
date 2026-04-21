




import os

# Constants
Testudo = '\U0001F438' 
empty_space = '_'
safe = ' '
veo = 'X'

def select_game_file():
    # Use os.walk to get files
    root, directories, files = next(os.walk('.'))
    
    # Filter for .testudo files
    testudo_files = [file for file in files if file.endswith('.testudo')]
    
    # Print available files with numbered list
    index = 1  
    for file in testudo_files:
        print(f"[{index}]\t{file}")
        index += 1
    
    # Get user selection
    while True:
            selection = input("Enter an option or filename: ")
            
            # Check if input is a number
            if selection.isdigit():
                index = int(selection) - 1
                if 0 <= index < len(testudo_files):
                    return testudo_files[index]
                else:
                    print("Invalid option. Please try again.")
            
            # Check if input is a filename
            elif selection in testudo_files:
                return selection
            
            else:
                print("Invalid input. Please try again.")

def load_game_file(filename):

    with open(filename, 'r') as file:
        # Read first line: rows, cols, jumps
        first_line = file.readline().strip().split()
        rows = int(first_line[0])
        cols = int(first_line[1])
        jumps = int(first_line[2])
        
        # Read speeds
        speeds_line = file.readline().strip().split()
        speeds = []
        for speed in speeds_line:
            speeds.append(int(speed))
        
        # Read board
        board = [list(file.readline().strip()) for _ in range(rows)]
    
    return rows, cols, jumps, speeds, board

def rotate_board(board, speeds):
    rotated_board = []
    for i in range(len(board)):
        row = board[i]
        speed = speeds[i]
        rotated_row = row[-speed:] + row[:-speed]
        rotated_board.append(rotated_row)
    
    return rotated_board

def check_collision(board, testudo_pos):
    row, col = testudo_pos
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return board[row][col] == empty_space
    return True

def display_board(board, testudo_pos, jumps_left):
    
    display_board = []
    for row in board:
        new_row = []
        for item in row:
            new_row.append(item) 
        display_board.append(new_row)
    
    # Place the testudo
    testudo_row, testudo_col = testudo_pos
    display_board[testudo_row][testudo_col] = Testudo
    
    # Print column numbers for reference
    print(" ", end=" ")
    for i in range(len(board[0])):
        print(f"{i:2}", end="")
    print()  
    
    # Print row numbers and board
    row_index = 0  
    for row in display_board:
        print(f"{row_index:2}", end=" ")  
        print("".join(row))
        row_index += 1
    
    # Print additional info
    print(f"Jumps left: {jumps_left}")

def move_testudo(board, current_pos, move, jumps_left):

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
            # Split the input to get coordinates
            parts = move.split()
            if len(parts) == 3:
                target_row = int(parts[1])
                target_col = int(parts[2])
                
                # Check if jump is valid (one row distance)
                if (abs(target_row - row) <= 1 and 
                    0 <= target_row < len(board) and 
                    0 <= target_col < len(board[0])):
                    return (target_row, target_col), jumps_left - 1
                else:
                    print("Invalid jump location. Must be within one row.")
            else:
                print("Invalid jump format. Use 'j row col'")

        else:
            print("No jumps left")
    
    return current_pos, jumps_left

def move_with_veo(board, testudo_pos, speeds):
    row, col = testudo_pos
    if board[row][col] == veo:
        veo_speed = speeds[row]
        col = (col + veo_speed) % len(board[row]) 
        return (row, col)
    return testudo_pos

def testudo_game(game_file):
    status = False

    # Load game configuration
    rows, cols, jumps, speeds, board = load_game_file(game_file)
    
    # Initial testudo position (one row above the obstacles)
    safe_row = [list(safe * cols)]  
    board = safe_row + board  
    speeds = [0] + speeds     
    testudo_pos = (0, cols // 2)
    
    # Add turn counter for display
    turn_count = 1  

    #create a safe row at the end which is the win condition
    safe_row_bottom = [list(safe * cols)]  
    board.append(safe_row_bottom[0])  
    speeds.append(0)  
    
    while not status:
        print(f"\nTurn {turn_count}")
        # Display the board
        display_board(board, testudo_pos, jumps)
        
        # Check for win condition (reached the bottom)
        if testudo_pos[0] == len(board) - 1:
            print("You won, Testudo made it to his exam!")
            status = True
            
        # Get user move
        move = input("WASDJ >> ")
        
        # Store previous position for collision check after rotation
        prev_pos = testudo_pos
        
        # Move the testudo
        testudo_pos, jumps = move_testudo(board, testudo_pos, move, jumps)

        
        # Rotate the board
        board = rotate_board(board, speeds)

        # If the testudo didn't move, shift it with the veo
        if testudo_pos == prev_pos:
            testudo_pos = move_with_veo(board, testudo_pos, speeds)
        
        # Check for collision after rotation
        if check_collision(board, testudo_pos):
            display_board(board, testudo_pos, jumps)
            print("You Lost, Sorry Testudo")
            status = True
              
        turn_count += 1

if __name__ == '__main__':
    selected_game_file = select_game_file()
    testudo_game(selected_game_file)