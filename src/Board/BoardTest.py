from src.Board.BoardPosition import BoardPosition
from src.Board.Board import Board
import pytest


@pytest.fixture()
def board_position():
    yield BoardPosition(x=0, y=0)


def test_can_create_a_bord():
    board = Board()
    assert board is not None


def test_board_has_tiles_in_a_3x3_space():
    board = Board()

    board_tiles = board.get_tiles()

    has_three_rows = len(board_tiles) == 3
    has_three_columns = len(board_tiles[0]) == 3 and len(
        board_tiles[1]) == 3 and len(board_tiles[2]) == 3

    assert has_three_rows
    assert has_three_columns


def test_all_tiles_are_empty_at_start():
    board = Board()

    board_tiles = board.get_tiles()

    for row in board_tiles:
        for tile in row:
            assert tile.is_empty() == True


def test_get_tile_with_board_position_0_0_should_return_first_tile():
    board = Board()

    result = board.get_tile(BoardPosition(0, 0))

    board_tiles = board.get_tiles()
    first_tile = board_tiles[0][0]

    assert result is first_tile


def test_get_tile_with_board_position_2_2_should_return_last_tile():
    board = Board()

    result = board.get_tile(BoardPosition(2, 2))

    board_tiles = board.get_tiles()
    last_tile = board_tiles[2][2]

    assert result is last_tile
