from src.Checker.Checker import Checker
from src.Board.BoardPosition import BoardPosition


class Tile():

    board_position: type[BoardPosition] = None
    checker: type[Checker] = None

    def __init__(self, board_position) -> None:
        if type(board_position) != BoardPosition:
            raise TypeError(
                f"Tile: board_position must be a Position. Received: {type(board_position)} - {board_position}")
        self.board_position = board_position

    def put_match(self, checker: type[Checker]) -> None:
        self.checker = checker

    def get_match(self) -> type[Checker]:
        return self.checker

    def is_empty(self) -> bool:
        return self.checker == None
