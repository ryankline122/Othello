import sys
import json
import socket
import random
from board import Board


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.player = 0
        self.board = Board()
        self.max_turn_time = 0

    def get_opponent(self):
        return 2 if self.player == 1 else 1

    def choose_move(self):
        """
        Identifies valid moves for the current board state and assigns
        weights to each move based on favorability.

        Corners are most favorable, followed by edge and center cells.
        """
        corners = [
            [0, 0],
            [0, 7],
            [7, 0],
            [7, 7],
        ]

        center = [
            [2, 2], [2, 3], [2, 4], [2, 5],
            [3, 2], [3, 3], [3, 4], [3, 5],
            [4, 2], [4, 3], [4, 4], [4, 5],
            [5, 2], [5, 3], [5, 4], [5, 5],
        ]

        moves = {}
        selected_move = []
        valid_moves = self.get_valid_moves(self.player)

        if valid_moves:
            for move in valid_moves:
                if move in corners:
                    moves[str(move)] = 999
                elif (move[0] == 0 or move[0] == 7) or (move[1] == 0 or move[1] == 7):
                    moves[str(move)] = 100
                elif move in center:
                    moves[str(move)] = 75
                else:
                    moves[str(move)] = 50

            selected_move = max(moves, key=moves.get)
            return selected_move
        else:
            print("Missing one or more valid moves. Forfeiting game")
            return [0, 0]

    def get_valid_moves(self, player=1, board=None):
        """
        Iterates over all cells in the board. If the current cell contains player
        token, check adjacent cells for opponent tokens. If found, look at the next cell
        in the same direction. Repeat while within bounds of the board or player token or empty
        space is found.

        Parameters:
        - player (int): The player to find valid moves for (default is player 1).
        - board (Board): The board to analyze (default is the Client's current instance of the board. Change this to look at future states of the board).

        """
        if board is None:
            board = self.board

        valid_moves = []
        opponent = 2 if player == 1 else 1

        for i in range(0, len(board.cells)):
            for j in range(0, len(board.cells[i])):
                current_cell = board.cells[i][j]

                if current_cell == player:
                    adjacent_cells = board.get_adjacent_cells(row=i, col=j)
                    for cell in adjacent_cells:
                        if board.cells[cell[0]][cell[1]] == opponent:
                            next_row = cell[0] + (cell[0] - i)
                            next_col = cell[1] + (cell[1] - j)

                            while 0 <= next_row < len(board.cells) and 0 <= next_col < len(board.cells[0]):
                                next_cell_value = board.cells[next_row][next_col]

                                if next_cell_value == player:
                                    break
                                elif next_cell_value == 0:
                                    valid_moves.append([next_row, next_col])
                                    break

                                next_row += cell[0] - i
                                next_col += cell[1] - j

        return valid_moves

    def prepare_response(self):
        move = self.choose_move()
        response = "{}\n".format(move).encode()
        print("sending {!r}".format(response))

        return response

    def parse_json_data(self, data):
        try:
            decoded_data = data.decode("UTF-8")
            json_data = json.loads(decoded_data)

            self.board.cells = json_data.get("board")
            self.max_turn_time = json_data.get("maxTurnTime")
            self.player = json_data.get("player")

        except (json.JSONDecodeError, UnicodeDecodeError, KeyError) as e:
            print(f"Error parsing JSON data: {e}")


if __name__ == "__main__":
    port = int(sys.argv[1]) if (len(sys.argv) > 1 and sys.argv[1]) else 1337
    host = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2]) else socket.gethostname()
    client = Client(host, port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        while True:
            data = sock.recv(1024)
            if not data:
                print("connection to server closed")
                break
            client.parse_json_data(data)
            print(client.player, client.max_turn_time, client.board)

            response = client.prepare_response()
            sock.sendall(response)

    finally:
        sock.close()
