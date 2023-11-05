from Tile import Tile
from BoardPosition import BoardPosition
from Match import Match, MatchType
import pytest


@pytest.fixture()
def board_position():
    yield BoardPosition(x=0, y=0)


def test_can_create_tile_with_board_position(board_position):
    tile = Tile(board_position)
    assert tile is not None


def test_create_tile_string_should_throw_an_error():
    with pytest.raises(TypeError):
        Tile("invalid_string")


def test_get_match_should_return_none_for_an_empty_tile(board_position):
    tile = Tile(board_position)
    assert tile.get_match() == None


def test_can_put_match_with_O_in_tile(board_position):
    tile = Tile(board_position)
    match_o = Match(MatchType.O)
    tile.put_match(match_o)
    assert tile.get_match() == match_o


def test_can_put_match_with_X_in_tile(board_position):
    tile = Tile(board_position)
    match_x = Match(MatchType.X)
    tile.put_match(match_x)
    assert tile.get_match() == match_x


def test_is_empty_should_return_true_for_an_tile_just_created(board_position):
    tile = Tile(board_position)
    assert tile.is_empty() == True


def test_is_empty_should_false_after_puting_a_match_in_a_tile(board_position):
    tile = Tile(board_position)
    tile.put_match(Match(MatchType.X))
    assert tile.is_empty() == False
