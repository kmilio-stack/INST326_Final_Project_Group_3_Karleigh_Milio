def select_game_file():
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



def testudo_game(game_file):
    dead = False

    # Load game configuration
    rows, cols, jumps, speeds, board = load_game_file(game_file)
    
    # Initial testudo position (one row above the cars)
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
    
    while not dead:
        print(f"\nTurn {turn_count}")
        # Display the board
        display_board(board, testudo_pos, jumps)
        
        # Check for win condition (reached the bottom)
        if testudo_pos[0] == len(board) - 1:
            print("You won, Testudo lives to cross another day!")
            dead = True
            
        
        # Check for collision
        if check_collision(board, testudo_pos):
            print("You Lost, Sorry Testudo")
            dead = True
            
        # Get user move
        move = input("WASDJ >> ")
        
        # Store previous position for collision check after rotation
        prev_pos = testudo_pos
        
        # Move testudo
        testudo_pos, jumps = move_testudo(board, testudo_pos, move, jumps)
        
        # Rotate the board
        board = rotate_board(board, speeds)
        
        # Check for collision after rotation
        if check_collision(board, testudo_pos):
            print("You Lost, Sorry Testudo")
            dead = True
            
            
        turn_count += 1