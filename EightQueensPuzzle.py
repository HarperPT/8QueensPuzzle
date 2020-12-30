# EightQueensPuzzle.py

class Puzzle:
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    QUEEN = 0
    NO_QUEEN = -1

    # -----------------------------------------------------------------------------------------------------------------
    def __init__(self, count):
        self.board = [[-1 for x in range(count)] for y in range(count)] 
        self.queens_count = count
        self.result_count = 0
        self.recurseNQ(self.board, 0)

    # -----------------------------------------------------------------------------------------------------------------
    def show_result(self):
        """
        Print the reuslt of the board. 
        """
        result = ""
        for row in self.board:
            for col in row:
                if col == -1:
                    result += "."
                else:
                    result += "Q"
            result += "\n"
        self.result_count += 1

        print ("The 8 queen puzzle result:　No.{}".format(self.result_count))    
        print (result)
    
    # -----------------------------------------------------------------------------------------------------------------
    def check_confilct(self, board, row, col):
        """
        Checking if there is any queen was on the route.

        :param board: The board map
        :param row: The current index of the row. 
        :param col: The current index of column.
        return: If there is queen in the route return False.  
        """
        
        # Check ← direction 
        for i in range(0, col):
            if board[row][i] == Puzzle.QUEEN:
                return False
        
        # Check ↖ direction
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == Puzzle.QUEEN:
                return False
            i -= 1
            j -= 1

        # Check ↙ direction
        i, j = row, col
        while i < self.queens_count and j >= 0:
            if board[i][j] == Puzzle.QUEEN:
                return False
            i += 1
            j -= 1

        return True

    # -----------------------------------------------------------------------------------------------------------------
    def recurseNQ(self, board, col):
        """
        Putting the queen on the board. If the mission completed, then print the board result

        :param board: The board map
        :param col: The current index of the col. 
        """
        if col == self.queens_count:
            self.show_result()

        for i in range(self.queens_count):
            if self.check_confilct(board, i, col):
                board[i][col] = Puzzle.QUEEN

                self.recurseNQ(board, col+1)
                
                board[i][col] = Puzzle.NO_QUEEN
        
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
queen_puzzle4 = Puzzle(4)
queen_puzzle8 = Puzzle(8)
