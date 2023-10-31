from Tile import Tile
from Match import Match, MatchType
# - Tile
#  Receive a match
#  Can be empty or filled


def test_can_create_tile_with_no_arguments():
    tile = Tile()
    assert tile is not None


def test_an_empty_tile_should_return_none():
    tile = Tile()
    assert tile.get_match() == None


def test_can_put_match_with_O_in_tile():
    tile = Tile()
    match_o = Match(MatchType.O)
    tile.put_match(match_o)
    assert tile.get_match() == match_o


def test_can_put_match_with_X_in_tile():
    tile = Tile()
    match_x = Match(MatchType.X)
    tile.put_match(match_x)
    assert tile.get_match() == match_x


# must be initialized with a position
