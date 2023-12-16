import sys
import json
import socket

class Client:
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.player = 0
    self.board = Board()
    self.max_turn_time = 0
  
  def get_move(self):
    # TODO
    return [2,4]
  
  def get_valid_moves(self):
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
    for i in range(0, len(self.board)):
      for j in range(0, len(self.board[i])):
        current_cell = self.board[i][j]
        
        if current_cell == self.player:
          # Do stuff
          pass
        else:
          continue
          
    
    
    return []

  def prepare_response(self):
    move = self.get_move()
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
