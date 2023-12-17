import pytest
from unittest.mock import patch
from client import Client

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
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        actual = board_instance.cells

        assert expected == actual

    def test_get_adjacent_cells_for_row_3_col_3(self, board_instance):
        expected = sorted(
            [[2, 2], [2, 3], [2, 4], [3, 2], [3, 4], [4, 2], [4, 3], [4, 4]]
        )
        actual = sorted(board_instance.get_adjacent_cells(row=3, col=3))

        assert expected == actual

    def test_get_adjacent_cells_for_top_left_corner(self, board_instance):
        expected = sorted([[0, 1], [1, 1], [1, 0]])
        actual = sorted(board_instance.get_adjacent_cells(row=0, col=0))

        assert expected == actual

    def test_get_adjacent_cells_for_top_right_corner(self, board_instance):
        expected = sorted([[0, 6], [1, 6], [1, 7]])
        actual = sorted(board_instance.get_adjacent_cells(row=0, col=7))

        assert expected == actual

    def test_get_adjacent_cells_for_bottom_left_corner(self, board_instance):
        expected = sorted([[6, 0], [6, 1], [7, 1]])
        actual = sorted(board_instance.get_adjacent_cells(row=7, col=0))

        assert expected == actual

    def test_get_adjacent_cells_for_bottom_right_corner(self, board_instance):
        expected = sorted([[6, 6], [6, 7], [7, 6]])
        actual = sorted(board_instance.get_adjacent_cells(row=7, col=7))

        assert expected == actual
