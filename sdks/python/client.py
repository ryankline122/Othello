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
    valid_moves = self.get_valid_moves()

    if valid_moves:
      return random.choice(valid_moves)
    else:
      # This shouldn't be hit, but sometimes it does
      print(self.board.cells)
      return [0,0]
  
  def get_valid_moves(self):
    # TODO: Improve me (if time allows)
    """
    Brute Force:
      - Iterate over all cells
      - If current cell == self.player:
          - if adjacent disc == opponent (ex. left is 2):
            - if the ___ adjacent cell to the opponent (ex. opponents left) is empty, valid
            - else if the ___ adjacent cell to the oppoennt is player disc, not valid
            - else the ___ adjacent cell to the opponent is another opponent disc, repeat
            - repeat for all adjacent cells
    """
    valid_moves = []
    
    for i in range(0, len(self.board.cells)):
      for j in range(0, len(self.board.cells[i])):
        current_cell = self.board.cells[i][j]
        
        if current_cell == self.player:
          adjacent_cells = self.board.get_adjacent_cells(row=i, col=j)
          for cell in adjacent_cells:
            if self.board.cells[cell[0]][cell[1]] == self.get_opponent():
              next_row = cell[0] + (cell[0] - i)
              next_col = cell[1] + (cell[1] - j)

              while 0 <= next_row < len(self.board.cells) and 0 <= next_col < len(self.board.cells[0]):
                next_cell_value = self.board.cells[next_row][next_col]

                if next_cell_value == self.player:
                  break
                elif next_cell_value == 0:
                  valid_moves.append([next_row, next_col])
                  break

                next_row += (cell[0] - i)
                next_col += (cell[1] - j)
        else:
          continue
          
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
