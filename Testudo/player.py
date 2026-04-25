class Player:
    """ represents the player character in the game.
    stores the score, jumps remaining, and current power-up"""
    
    def __init__(self, start_row, start_col, name="Testudo", jumps_left=3):
        """ initialize player object.
        Args: 
            name (str): name of the player character
            jumps_left (int): number of jumps the player has remaining
        """
        self.name = name
        self.jumps_left = jumps_left
        self.active_power_up = None
        self.row = start_row
        self.col = start_col
        
    def get_position(self):
        """ returns the current position of the player as a tuple (row, col) """
        return (self.row, self.col)
    
    def move(self, board, move):
        """ handles player movement and jump logic.
        Args:
            board (list): game board
            move (str): player input
            
        Returns:
            None
        """
        move = move.lower()
        
        if move == 'w' and self.row > 0:
            self.row -= 1
            
        elif move == 's' and self.row < len(board) - 1:
            self.row += 1
            
        elif move == 'a' and self.col > 0:
            self.col -= 1
            
        elif move == 'd' and self.col < len(board[0]) - 1:
            self.col += 1
        
        elif move.startswith('j'):
            self.jump(board, move)
            
    def jump(self, board, move):
        """ handles player jump logic.
        Args:
            board (list): game board
            move (str): player input
            
        Returns:
            None
        """
        if self.jumps_left <= 0:
            print("No jumps left")
            return
        
        parts = move.split()
        
        if len(parts) != 3:
            print("Invalid jump format. Use 'j row col'")
            return  
        target_row = int(parts[1])
        target_col = int(parts[2])
        
        if (abs(target_row - self.row) <= 1 and 
            0 <= target_row < len(board) and 
            0 <= target_col < len(board[0])):
            self.row = target_row
            self.col = target_col
            self.jumps_left -= 1
            
        else:
            print("Invalid jump location. Must be within one row.")
    

