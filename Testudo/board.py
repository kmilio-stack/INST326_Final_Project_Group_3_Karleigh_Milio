# Constants
TESTUDO = '\U0001F422'
EMPTY_SPACE = '_'
SAFE = ' '

class Board:
    """Represents the game board for Testudo."""
    
    def __init__(self, grid, speeds):
        """Initializes the Board object.
        
        Args:
            grid (list): 2D list representing the game board.
            speeds (list): movement speed per row.
        
        Returns:
            None"""
        
        self.grid = grid
        self.speeds = speeds
        
    def rotate(self):
        """
        Rotates each row of the board based on its speed.
        
        Returns:
            list: rotated board
            
        Author:
            Brevard
        """
        rotated = []
        
        for i in range(len(self.grid)):
            row = self.grid[i]
            
            if len(row) == 0:
                rotated.append(row)
                continue
            
            speed = self.speeds[i] % len(row)
            
            rotated_row = row[-speed:] + row[:-speed]
            rotated.append(rotated_row)
        
        self.grid = rotated
        return self.grid
    
    def check_collision(self, testudo_pos):
        """
        Checks if the player collided with an obstacle.
        
        Args:
            testudo_pos (tuple): (row, col) position of player
        
        Returns:
            bool: True if a collision occurs otherwise false.
        
        Author:
            Brevard
        """
        row, col = testudo_pos
        return self.grid[row][col] not in {EMPTY_SPACE, SAFE}
    
    def display(self, testudo_pos, jumps_left):
        """
        Displays the current state of the board.
        
        Args:
            testudo_pos (tuple): player position
            jumps_left (int): remaining jumps
            
        Returns:
            None
        
        Author:
            Brevard
        
        Techniques Claimed:
             F-strings containing expressions; comprehensions and generator expressions
        """
        if not self.grid:
            print("Empty Board")
            return
        
        temp_board = [row[:] for row in self.grid]
        
        row, col = testudo_pos
        temp_board[row][col] = TESTUDO
        
        header = "  " + "".join(f"{i:2}" for i in range(len(self.grid[0])))
        print(header)
        
        for i, row in enumerate(temp_board):
            print(f"{i:2} " + "".join(row))
        
        print(f"Jumps left: {jumps_left}")

