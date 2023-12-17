import pytest
from unittest.mock import patch
from client import Client

class TestClient:
    def test_get_move_returns_a_valid_move(self, client_instance):
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        assert client_instance.choose_move() != None

    @patch("client.Client.choose_move")
    def test_prepare_response_returns_a_valid_response(
        self, mock_choose_move, client_instance
    ):
        client_instance.choose_move.return_value = [2, 4]
        assert client_instance.prepare_response() == b"[2, 4]\n"
    
    