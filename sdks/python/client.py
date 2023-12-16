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
    # TODO: Improve me
    """
    Strategies:
    - Corners are most valuable (cannot be flipped)
    - Not recommended to take cells adjacent to corners
    - Focus on limiting opponents options and increasing yours instead of just number of discs on the board
    - Focus on initial 4x4 central area at the start of the game.
    """
    corners = [
      [0,0],
      [0,7],
      [7,0],
      [7,7],
    ]
    
    options = {}
    
    valid_moves = self.get_valid_moves(self.player)
    valid_moves_for_opponent = self.get_valid_moves(self.get_opponent)
    selected_move = []

    if valid_moves:
      for move in valid_moves:
        # Prioritize corners
        if move in corners:
          return move
        else:
          next_board = self.board.what_if(row=move[0], col=move[1], player=self.player)
          next_board_valid_moves = self.get_valid_moves(self.player, board=next_board)
          next_board_valid_moves_for_opponent = self.get_valid_moves(self.get_opponent, board=next_board)
          next_board_disc_count = self.board.get_discs_for_player(player=self.player)
          increases_opponent_options = 0.5 if len(next_board_valid_moves_for_opponent) > len(valid_moves_for_opponent) else 1
          
          options[str(move)] = ((len(next_board_valid_moves) - len(next_board_valid_moves_for_opponent)) + next_board_disc_count) * increases_opponent_options
      
      print(f"Options: {options}")
      selected_move = max(options, key=options.get)
      return selected_move
    else:
      print("Missing one or more valid moves. Forfeiting game")
      print(self.board.cells)
      return [0,0]
  
  def get_valid_moves(self, player=1, board=None):
    # TODO: Improve me (if time allows)
    """
    Brute Force:
      - Iterate over all cells
      - If current cell == self.player:
          - if adjacent disc == opponent (ex. left is 2):
            - if the ___ adjacent cell to the opponent (ex. opponents left) is empty, valid
            - else if the ___ adjacent cell to the opponent is player disc, not valid
            - else the ___ adjacent cell to the opponent is another opponent disc, repeat
            - repeat for all adjacent cells
    """
    if board is None:
      board = self.board
    
    valid_moves = []

    for i in range(0, len(board.cells)):
      for j in range(0, len(board.cells[i])):
        current_cell = board.cells[i][j]
        
        if current_cell == player:
          adjacent_cells = board.get_adjacent_cells(row=i, col=j)
          for cell in adjacent_cells:
            if board.cells[cell[0]][cell[1]] == self.get_opponent():
              next_row = cell[0] + (cell[0] - i)
              next_col = cell[1] + (cell[1] - j)

              while 0 <= next_row < len(board.cells) and 0 <= next_col < len(board.cells[0]):
                next_cell_value = board.cells[next_row][next_col]

                if next_cell_value == player:
                  break
                elif next_cell_value == 0:
                  valid_moves.append([next_row, next_col])
                  break

                next_row += (cell[0] - i)
                next_col += (cell[1] - j)
          
    return valid_moves 

  def prepare_response(self):
    move = self.choose_move()
    response = '{}\n'.format(move).encode()
    print('sending {!r}'.format(response))
    
    return response
  
  def parse_json_data(self, data):
    try:
      decoded_data = data.decode('UTF-8')
      json_data = json.loads(decoded_data)
      
      self.board.cells = json_data.get('board')
      self.max_turn_time = json_data.get('maxTurnTime')
      self.player = json_data.get('player')
    
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
        print('connection to server closed')
        break
      client.parse_json_data(data)
      print(client.player, client.max_turn_time, client.board)

      response = client.prepare_response()
      sock.sendall(response)
  
  finally:
    sock.close()
