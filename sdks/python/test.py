import pytest
from unittest.mock import patch
from client import Client

class TestGetMove:
  def test_get_move_returns_a_valid_move(self, client_instance):
    board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    assert client_instance.choose_move() != None

class TestPrepareResponse:
  @patch("client.Client.choose_move")
  def test_prepare_response_returns_a_valid_response(self, mock_choose_move, client_instance):
    client_instance.choose_move.return_value = [2,4]
    assert client_instance.prepare_response() == b'[2, 4]\n'

class TestGetValidMoves:
  def test_get_valid_moves_on_new_game(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 1, 2, 0, 0, 0], 
      [0, 0, 0, 2, 1, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected = sorted([[2, 4], [3, 5], [5, 3], [4, 2]])
    actual = sorted(client_instance.get_valid_moves())

    assert expected == actual
  
  def test_get_valid_moves_edge_upper(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 2, 0, 0, 0, 0], 
      [0, 0, 0, 1, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected = [[0, 3]]
    actual = sorted(client_instance.get_valid_moves())

    assert expected == actual

  def test_get_valid_moves_edge_upper_left(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 2, 0, 0, 0, 0], 
      [0, 0, 0, 0, 1, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected = [[0,2]]
    actual = client_instance.get_valid_moves()

    assert expected == actual

  def test_get_valid_moves_edge_left(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [0, 2, 1, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected = [[0,0]]
    actual = client_instance.get_valid_moves()
    
    assert expected == actual

  def test_get_valid_moves_edge_lower_left(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 1, 0, 0, 0, 0, 0], 
      [0, 2, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected = [[7,0]]
    actual = client_instance.get_valid_moves()
    
    assert expected == actual

  def test_get_valid_moves_edge_bottom(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 1, 0, 0, 0, 0], 
      [0, 0, 0, 2, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected = [[7,3]]
    actual = client_instance.get_valid_moves()
    
    assert expected == actual

  def test_get_valid_moves_edge_bottom_right(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [1, 0, 0, 0, 0, 0, 0, 0], 
      [0, 2, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected = [[7,2]]
    actual = client_instance.get_valid_moves()
    
    assert expected == actual


  def test_get_valid_moves_edge_right(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [0, 0, 0, 0, 0, 1, 2, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected = [[0,7]]
    actual = client_instance.get_valid_moves()
    
    assert expected == actual
    
  def test_get_valid_moves_edge_upper_right(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 2, 0, 0], 
      [0, 0, 0, 0, 1, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected = [[0,6]]
    actual = client_instance.get_valid_moves()
    
    assert expected == actual

  def test_get_valid_moves_endgame1(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [1, 1, 1, 0, 2, 2, 2, 2], 
      [1, 1, 1, 1, 2, 2, 2, 2], 
      [1, 2, 1, 2, 1, 1, 2, 2], 
      [1, 1, 1, 2, 1, 1, 2, 2], 
      [1, 1, 1, 2, 1, 2, 2, 2], 
      [0, 1, 2, 1, 1, 2, 1, 2], 
      [1, 2, 1, 1, 1, 1, 1, 2], 
      [2, 2, 2, 2, 2, 2, 2, 2]
    ]
    
    expected =[[0,3]]
    actual = client_instance.get_valid_moves()

    assert expected == actual

  def test_get_valid_moves_endgame2(self, client_instance, board_instance):
    client_instance.player = 1
    client_instance.board = board_instance
    board_instance.cells = [
      [1, 1, 1, 1, 1, 1, 1, 1], 
      [0, 2, 2, 2, 2, 2, 2, 2], 
      [1, 2, 2, 2, 1, 1, 2, 2], 
      [1, 2, 1, 2, 1, 2, 2, 2], 
      [1, 2, 1, 1, 2, 2, 1, 2], 
      [1, 2, 1, 2, 1, 2, 1, 2], 
      [1, 1, 1, 1, 2, 1, 2, 2], 
      [1, 2, 2, 2, 2, 2, 2, 2]
    ]
      
    expected = [[1,0]]
    actual = client_instance.get_valid_moves()

    assert expected == actual

class TestBoard:
  def test_board_should_be_empty_on_init(self, board_instance):
    expected = [
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0]      
    ]
    actual = board_instance.cells

    assert expected == actual
  
  def test_get_adjacent_cells_for_row_3_col_3(self, board_instance):
    expected = [[2,2], [2,3], [2,4], [3,2], [3,4], [4,2], [4,3], [4,4]]
    actual = board_instance.get_adjacent_cells(row=3, col=3)
  
  def test_get_adjacent_cells_for_top_left_corner(self, board_instance):
    expected = [[0,1], [1,1], [1,0]]
    actual = board_instance.get_adjacent_cells(row=0, col=0)

  def test_get_adjacent_cells_for_top_right_corner(self, board_instance):
    expected = [[0,6], [1,6], [1,7]]
    actual = board_instance.get_adjacent_cells(row=0, col=7)

  def test_get_adjacent_cells_for_bottom_left_corner(self, board_instance):
    expected = [[6,0], [6,1], [7,1]]
    actual = board_instance.get_adjacent_cells(row=7, col=0)

  def test_get_adjacent_cells_for_bottom_right_corner(self, board_instance):
    expected = [[6,6], [6,7], [7,6]]
    actual = board_instance.get_adjacent_cells(row=7, col=7)