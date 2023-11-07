from src.Checker.Checker import Checker
from src.Board.BoardPosition import BoardPosition
from src.Board.Board import Board
from src.Tile.Tile import Tile


class Move:

    checker: type[Checker] = None
    position: type[BoardPosition] = None
    board: type[Board] = None
    already_executed: bool = False

    def __init__(self, checker: type[Checker], position: type[BoardPosition], board: type[Board]) -> None:
        self.checker = checker
        self.position = position
        self.board = board
        self.already_executed = False

    def execute(self):
        if self.already_executed:
            raise RuntimeError('This move was already executed')

        tile: type[Tile] = self.board.get_tile(self.position)
        tile.put_match(self.checker)
        self.already_executed = True
