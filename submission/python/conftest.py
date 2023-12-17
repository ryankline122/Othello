import pytest
from client import Client
from board import Board


@pytest.fixture
def client_instance():
    return Client(host="localhost", port=8000)


@pytest.fixture
def board_instance():
    return Board()
