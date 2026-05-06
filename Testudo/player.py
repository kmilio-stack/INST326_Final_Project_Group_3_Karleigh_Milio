class Player:
    """ represents the player character in the game.
    stores the score, jumps remaining, and current position of the player."""
    
    def __init__(self, start_row, start_col, name="Testudo", jumps_left=0):
        """ Initializes a player object
        
        Args:
            start_row (int): starting row position
            start_col (int): starting column position
            name (str): player name
            jumps_left (int): number of jumps the player starts with
            
        Author: Milio
        
        """
        self.name = name
        self.jumps_left = jumps_left
        self.row = start_row
        self.col = start_col
        
    def get_position(self):
        """ returns the current position of the player as a tuple (row, col) 
        Returns:
            tuple: (row, col) position of the player
        
        Author: Milio
        """
        return (self.row, self.col)
    
    def move(self, board, move_choice):
        """ handles player movement and jump logic.
        Args:
            board (list): game board
            move_choice (str): player input for movement, 
            ("w", "a", "s", "d" for movement or "j row col" for jump)
            
        Returns:
            None
        
        Author: Milio
        Technique claimed: sequence unpacking
        """
        move_choice = move_choice.lower().strip()
        
        if move_choice == "w" and self.row > 0:
            self.row -= 1
            
        elif move_choice == "s" and self.row < len(board.grid) - 1:
            self.row += 1
            
        elif move_choice == "a" and self.col > 0:
            self.col -= 1
            
        elif move_choice == "d" and self.col < len(board.grid[0]) - 1:
            self.col += 1
        
        elif move_choice.startswith("j"):
            self.jump(board, move_choice)
            
        else:
            print("Invalid move. Use w, a, s, d for movement or j row col for jump.")
    
    def jump(self, board, move_choice):
        """ Handles player jump logic.
        Args:
            board (list): game board object
            move_choice (str): player input in format "j row col"
            
        Returns:
            None
            
        Author: Milio
        Technique claimed: Conditional expression
        """
        if self.jumps_left <= 0:
            print("No jumps left")
            return
        
        parts = move_choice.split()
        
        if len(parts) != 3:
            print("Invalid jump format. Use j row col.")
            return 
        
        try:
            command, target_row, target_col = parts
            target_row = int(target_row)
            target_col = int(target_col)
            
        except ValueError:
            print("Invalid jump format. Row and column must be integers.")
            return
        
        valid_row = 0 <= target_row < len(board.grid)
        valid_col = 0 <= target_col < len(board.grid[0])
        
        close_enough = (
            abs(target_row - self.row) <= 1)
        
        if valid_row and valid_col and close_enough:    
            self.row = target_row
            self.col = target_col
            self.jumps_left -= 1
            
        else:
            reason = "off the board" if not (valid_row and valid_col) else "too far away"
            
            print(f"Invalid jump location: {reason}.")
                  
