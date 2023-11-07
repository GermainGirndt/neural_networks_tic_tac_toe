from src.Match.Match import Match
from src.Board.BoardPosition import BoardPosition


class Tile():

    board_position: type[BoardPosition] = None
    match: type[Match] = None

    def __init__(self, board_position) -> None:
        if type(board_position) != BoardPosition:
            raise TypeError(
                f"Tile: board_position must be a Position. Received: {type(board_position)} - {board_position}")
        self.board_position = board_position

    def put_match(self, match: type[Match]) -> None:
        self.match = match

    def get_match(self) -> type[Match]:
        return self.match

    def is_empty(self) -> bool:
        return self.match == None
