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

        if col > 0:
            adjacent_cells.append((row, col - 1))
        if col < num_cols - 1:
            adjacent_cells.append((row, col + 1))
        if row > 0:
            adjacent_cells.append((row - 1, col))
        if row < num_rows - 1:
            adjacent_cells.append((row + 1, col))

        return adjacent_cells 
    