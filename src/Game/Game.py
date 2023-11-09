from src.Player.Player import Player
from src.Board.Board import Board
from enum import Enum


class GameState(Enum):
    NOT_STARTED = 0
    NOW_PLAYING = 1


class Game():

    board: type[Board] = None
    player_one: type[Player] = None
    player_two: type[Player] = None
    game_state: type[GameState] = GameState.NOT_STARTED

    next_player: type[Player] = None

    def __init__(self, board: type[Board], player_one: type[Player], player_two: type[Player]):
        self.board = board
        self.player_one = player_one
        self.player_two = player_two
        self.game_state = GameState.NOT_STARTED
        self.next_player = None
        self.validate_players()

    def validate_players(self):
        if self.player_one.has_same_checker_type(self.player_two):
            raise TypeError("Players must have different checker types")

    def get_state(self):
        return self.game_state

    def start(self, start_player: type[Player]):

        if type(start_player) != Player:
            raise TypeError(
                f"Game: start_player must be a Player. Received: {type(start_player)} - {start_player}")

        if start_player not in [self.player_one, self.player_two]:
            raise RuntimeError(
                f"Game: start_player must be one of the game players. Received: {start_player}")

        if self.game_state == GameState.NOW_PLAYING:
            raise RuntimeError(
                "Game: Cannot restart the game which has already been started")

        self.game_state = GameState.NOW_PLAYING
        self.next_player = start_player

    def get_next_player(self):

        if self.game_state == GameState.NOT_STARTED:
            raise RuntimeError("Game has not started yet")

        return self.next_player
