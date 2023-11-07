import pytest
from src.Move.Move import Move
from src.Checker.Checker import Checker, CheckerType
from src.Board.Board import Board
from src.Board.BoardPosition import BoardPosition


def test_can_create_a_move_for_an_empty_board():

    checker = Checker(CheckerType.O)
    position = BoardPosition(0, 0)
    board = Board()
    move = Move(checker=checker, position=position, board=board)

    assert move is not None


def test_can_execute_a_move_for_an_empty_board():

    checker = Checker(CheckerType.O)
    position = BoardPosition(0, 0)
    board = Board()
    move = Move(checker=checker, position=position, board=board)

    assert board.get_tile(position).is_empty() is True
    move.execute()
    assert board.get_tile(position).is_empty() is False


def test_cannot_execute_the_same_move_two_times():

    checker = Checker(CheckerType.O)
    position = BoardPosition(0, 0)
    board = Board()
    move = Move(checker=checker, position=position, board=board)
    move.execute()
    with pytest.raises(RuntimeError):
        move.execute()
