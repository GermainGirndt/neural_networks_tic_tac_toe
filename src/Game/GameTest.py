import pytest

from src.Game.Game import Game, GameState
from src.Player.Player import Player
from src.Board.Board import Board
from src.Board.BoardPosition import BoardPosition
from src.Checker.Checker import Checker, CheckerType


def test_can_create_a_game():

    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)
    assert game is not None


def test_create_game_with_player_using_the_same_checks_should_throw_an_error():
    player_x_one = Player(CheckerType.X)
    player_x_two = Player(CheckerType.X)
    board = Board()
    with pytest.raises(TypeError):
        Game(board, player_x_one, player_x_two)


def test_start_game_should_return_change_game_state_to_now_playing():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)

    assert game.get_state() is GameState.NOT_STARTED
    game.start(player_x)
    assert game.get_state() is GameState.NOW_PLAYING


def test_start_game_should_throw_error_if_a_string_is_passed():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)

    with pytest.raises(TypeError):
        game.start("invalid_string")


def test_get_next_player_should_throw_an_error_if_game_is_not_started():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)

    with pytest.raises(RuntimeError):
        game.get_next_player()


def test_start_game_which_has_already_started_should_throw_error():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)
    game.start(player_x)

    with pytest.raises(RuntimeError):
        game.start(player_x)


def test_cannot_start_game_with_player_not_set():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)

    other_player_x = Player(CheckerType.X)
    with pytest.raises(RuntimeError):
        game.start(other_player_x)


def test_start_game_should_return_first_player_correctly_after_game_has_been_started():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)

    game.start(player_x)
    assert game.get_next_player() is player_x


def test_end_turn_should_thow_an_error_if_game_has_not_started_yet():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)

    with pytest.raises(RuntimeError):
        game.end_turn(player_x)


def test_end_turn_should_thow_an_error_if_players_is_not_playing():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)
    game.start(player_x)

    player_not_playing = Player(CheckerType.O)

    with pytest.raises(RuntimeError):
        game.end_turn(player_not_playing)


def test_end_turn_should_thow_an_error_if_it_is_not_players_turn():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)
    game.start(player_x)

    with pytest.raises(RuntimeError):
        game.end_turn(player_o)


def test_end_turn_should_change_next_player_if_the_game_has_started():
    player_x = Player(CheckerType.X)
    player_o = Player(CheckerType.O)
    board = Board()
    game = Game(board, player_x, player_o)
    game.start(player_x)

    assert game.get_next_player() is player_x
    game.end_turn(player_x)
    assert game.get_next_player() is player_o
    game.end_turn(player_o)
    assert game.get_next_player() is player_x
