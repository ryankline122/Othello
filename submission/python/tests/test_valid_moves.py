import pytest
from unittest.mock import patch
from client import Client

class TestValidMoves:
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
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = sorted([[2, 4], [3, 5], [5, 3], [4, 2]])
        actual = sorted(client_instance.get_valid_moves())

        assert expected == actual

    def test_get_valid_moves_for_opponent(self, client_instance, board_instance):
        client_instance.player = 2
        client_instance.board = board_instance
        board_instance.cells = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = sorted([[2, 4], [3, 5], [5, 3], [4, 2]])
        actual = sorted(client_instance.get_valid_moves(client_instance.get_opponent()))

        assert expected == actual

    def test_get_valid_moves_check_diagonals(self, client_instance, board_instance):
        client_instance.player = 1
        client_instance.board = board_instance
        board_instance.cells = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 2, 1, 2, 0, 0, 0],
            [0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = sorted(
            [[1, 1], [1, 3], [1, 5], [3, 5], [5, 5], [5, 3], [5, 1], [3, 1]]
        )
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
            [0, 0, 0, 0, 0, 0, 0, 0],
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
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = [[0, 2]]
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
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = [[0, 0]]
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
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = [[7, 0]]
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
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = [[7, 3]]
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
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = [[7, 2]]
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
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = [[0, 7]]
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
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected = [[0, 6]]
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
            [2, 2, 2, 2, 2, 2, 2, 2],
        ]

        expected = [[0, 3]]
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
            [1, 2, 2, 2, 2, 2, 2, 2],
        ]

        expected = [[1, 0]]
        actual = client_instance.get_valid_moves()

        assert expected == actual
