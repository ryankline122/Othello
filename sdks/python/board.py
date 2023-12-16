class Board:
    def __init__(self):
        self.cells = [
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    def get_adjacent_cells(self, row, col):
        adjacent_cells = []
        num_rows = len(self.cells)
        num_cols = len(self.cells[0]) if self.cells else 0

        # Horizontal and vertical directions
        if col > 0:
            adjacent_cells.append([row, col - 1])
        if col < num_cols - 1:
            adjacent_cells.append([row, col + 1])
        if row > 0:
            adjacent_cells.append([row - 1, col])
        if row < num_rows - 1:
            adjacent_cells.append([row + 1, col])

        # Diagonal directions
        if row > 0 and col > 0:
            adjacent_cells.append([row - 1, col - 1])
        if row > 0 and col < num_cols - 1:
            adjacent_cells.append([row - 1, col + 1])
        if row < num_rows - 1 and col > 0:
            adjacent_cells.append([row + 1, col - 1])
        if row < num_rows - 1 and col < num_cols - 1:
            adjacent_cells.append([row + 1, col + 1])

        return adjacent_cells

    def what_if(self, row, col, player):
        cells = self.cells.copy()
        cells[row][col] = player

        next_board = Board()
        next_board.cells = cells

        return next_board
    
    def get_discs_for_player(self, player):
        count = 0
        
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[i])):
                current_cell = self.cells[i][j]

                if current_cell == player:
                    count +=1
                    
        return count