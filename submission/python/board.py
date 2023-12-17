class Board:
    def __init__(self):
        """
        Initializes a new Othello board with all cells set to 0.

        The board is represented as a 2D list where each element corresponds to a cell
        on the board. A value of 0 represents an empty cell.

        Example:
            >>> board = Board()
        """
        self.cells = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def get_adjacent_cells(self, row, col):
        """
        Returns a list of coordinates representing adjacent cells to the given cell.

        Parameters:
        - row (int): The row index of the cell.
        - col (int): The column index of the cell.

        Returns:
        list of list: A list of coordinate pairs representing adjacent cells.
        """
        adjacent_cells = []
        num_rows = len(self.cells)
        num_cols = len(self.cells[0]) if self.cells else 0

        if col > 0:
            adjacent_cells.append([row, col - 1])
        if col < num_cols - 1:
            adjacent_cells.append([row, col + 1])
        if row > 0:
            adjacent_cells.append([row - 1, col])
        if row < num_rows - 1:
            adjacent_cells.append([row + 1, col])

        if row > 0 and col > 0:
            adjacent_cells.append([row - 1, col - 1])
        if row > 0 and col < num_cols - 1:
            adjacent_cells.append([row - 1, col + 1])
        if row < num_rows - 1 and col > 0:
            adjacent_cells.append([row + 1, col - 1])
        if row < num_rows - 1 and col < num_cols - 1:
            adjacent_cells.append([row + 1, col + 1])

        return adjacent_cells

    def get_discs_for_player(self, player):
        """
        Counts and returns the number of discs on the board for a given player.

        Parameters:
        - player (int): The player for whom to count the discs.

        Returns:
        int: The number of discs belonging to the specified player on the board.
        """
        count = 0

        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[i])):
                current_cell = self.cells[i][j]

                if current_cell == player:
                    count += 1

        return count
