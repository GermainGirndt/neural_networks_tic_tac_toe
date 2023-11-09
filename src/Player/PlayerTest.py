import pytest
from src.Player.Player import Player
from src.Board.BoardPosition import BoardPosition
from src.Checker.Checker import Checker, CheckerType
from src.Move.Move import Move
from src.Board.Board import Board
from unittest.mock import MagicMock

# - Players (2)
#   Either X or O
#   Place a checker into a board's tile


@pytest.fixture()
def board_position():
    yield BoardPosition(x=0, y=0)


def test_create_player_without_checker_type_should_throw_error():
    with pytest.raises(TypeError):
        Player()


def test_can_create_player_with_checker_type_O():
    player = Player(CheckerType.O)
    assert player is not None


def test_can_create_player_with_checker_type_X():
    player = Player(CheckerType.X)
    assert player is not None


def test_has_same_checker_type_should_return_true_if_checker_types_are_equal():
    player_one = Player(CheckerType.O)
    player_two = Player(CheckerType.O)

    assert player_one.has_same_checker_type(player_two) is True


def test_has_same_checker_type_should_return_false_if_checker_types_are_different():
    player_one = Player(CheckerType.O)
    player_two = Player(CheckerType.X)

    assert player_one.has_same_checker_type(player_two) is False


def test_has_same_checker_type_should_throw_an_error_if_used_with_string():
    player_one = Player(CheckerType.O)

    with pytest.raises(TypeError):
        player_one.has_same_checker_type("invalid")


def test_player_can_execute_move():

    checker = Checker(CheckerType.O)
    position = BoardPosition(0, 0)
    board = Board()
    move = Move(checker=checker, position=position, board=board)
    player = Player(CheckerType.O)
    mocked_execute_method = MagicMock(return_value=None)

    move.execute = mocked_execute_method

    player.execute(move)

    mocked_execute_method.assert_called_once()


def test_should_throw_error_if_execute_move_has_different_checker_than_player():
    checker = Checker(CheckerType.O)
    position = BoardPosition(0, 0)
    board = Board()
    move = Move(checker=checker, position=position, board=board)
    player = Player(CheckerType.X)

    with pytest.raises(TypeError):
        player.execute(move)


def test_should_throw_error_if_execute_is_called_with_a_string():
    player = Player(CheckerType.X)

    with pytest.raises(TypeError):
        player.execute("invalid")
