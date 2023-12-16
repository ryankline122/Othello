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
            adjacent_cells.append((row, col - 1))
        if col < num_cols - 1:
            adjacent_cells.append((row, col + 1))
        if row > 0:
            adjacent_cells.append((row - 1, col))
        if row < num_rows - 1:
            adjacent_cells.append((row + 1, col))

        # Diagonal directions
        if row > 0 and col > 0:
            adjacent_cells.append((row - 1, col - 1))
        if row > 0 and col < num_cols - 1:
            adjacent_cells.append((row - 1, col + 1))
        if row < num_rows - 1 and col > 0:
            adjacent_cells.append((row + 1, col - 1))
        if row < num_rows - 1 and col < num_cols - 1:
            adjacent_cells.append((row + 1, col + 1))

        return adjacent_cells

    