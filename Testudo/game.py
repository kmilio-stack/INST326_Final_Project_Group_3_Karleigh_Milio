import os
from board import Board, SAFE
from player import Player


class TestudoGame:
    def __init__(self):
        """Initializes TestudoGame object with game state values"""
        self.rows = 0
        self.cols = 0
        self.jumps = 0
        self.speeds = []
        self.board = []
        self.player = (0, 0)
        self.turn_count = 1
        self.dead = False


    def select_game_file(self):
        """Displays available .testudo files and allows the user to select one.

            Returns:
                str: Selected filename
        """
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

    def load_game_file(self, filename):
        """Loads game configuration from a file.

            Args:
                filename (str): The name of the file to load

            Returns:
                self.rows, self.cols, self.jumps, self.speeds, self.board
        """

        with open(filename, 'r') as file:
            # Read first line: rows, cols, jumps
            first_line = file.readline().strip().split()
            self.rows = int(first_line[0])
            self.cols = int(first_line[1])
            self.jumps = int(first_line[2])
            
            # Read speeds
            speeds_line = file.readline().strip().split()
            self.speeds = []
            for speed in speeds_line:
                self.speeds.append(int(speed))
            
            # Read board
            self.board = [list(file.readline().strip()) for _ in range(self.rows)]

    def setup_game(self):
        """Sets up the initial game board, including safe zones and starting position"""
        
        # Initial testudo position (one row above the obstacles)
        safe_row = [list(SAFE * self.cols)]
        self.board = safe_row + self.board
        self.speeds = [0] + self.speeds
     
        #create a safe row at the end which is the win condition
        safe_row_bottom = [list(SAFE * self.cols)]
        self.board.append(safe_row_bottom[0])
        self.speeds.append(0)  
        
        # convert list to Board object
        self.board = Board(self.board, self.speeds)
        
        #create player object
        self.player = Player(0, self.cols // 2, jumps_left=self.jumps)
        
        
    def run(self): 
        """Runs the main game loop until the player wins or loses."""
        
        while not self.dead:
            print(f"\nTurn {self.turn_count}")
            # Display the board
            self.board.display(self.player.get_position(),
                               self.player.jumps_left)
            
            # Check for win condition (reached the bottom)
            if self.player.row == len(self.board.grid) - 1:
                print("You won, Testudo lives to cross another day!")
                self.dead = True
                return
                
            # Check for collision
            if self.board.check_collision(self.player.get_position()):
                print("You Lost, Sorry Testudo")
                self.dead = True
                return 
            
            # Get user move
            move_choice = input("WASD or j row col >> ")
             
            # move the player based on user input 
            self.player.move(self.board, move_choice)
            
           # Check collision after move
            if self.board.check_collision(
                self.player.get_position()):
                print("You Lost, Sorry Testudo")
                self.dead = True
                return
           
            # Rotate the board
            self.board.rotate()
            
            # Check for collision after rotation
            if self.board.check_collision(self.player.get_position()):
                print("You Lost, Sorry Testudo")
                self.dead = True
                return
            
            self.turn_count += 1
            
if __name__ == "__main__":
    game = TestudoGame()
    filename = game.select_game_file()
    
    if filename is not None:
        game.load_game_file(filename)
        game.setup_game()
        game.run()