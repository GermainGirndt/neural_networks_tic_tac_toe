from src.Checker.Checker import Checker
from src.Board.BoardPosition import BoardPosition
from src.Board.Board import Board
from src.Tile.Tile import Tile


class Move:

    checker: type[Checker] = None
    position: type[BoardPosition] = None
    board: type[Board] = None

    def __init__(self, checker: type[Checker], position: type[BoardPosition], board: type[Board]) -> None:
        self.checker = checker
        self.position = position
        self.board = board
        self.validate_tile_is_free()

    def execute(self):
        self.validate_tile_is_free()

        tile: type[Tile] = self.board.get_tile(self.position)
        tile.put_match(self.checker)

    def validate_tile_is_free(self):
        tile: type[Tile] = self.board.get_tile(self.position)

        if not tile.is_empty():
            raise RuntimeError('This move was already executed')
