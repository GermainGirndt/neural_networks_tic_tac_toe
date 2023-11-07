

from src.Position.Position import Position


class BoardPosition(Position):

    x = -1
    y = -1

    def __init__(self, x, y) -> None:
        if not (0 <= x <= 2):
            raise ValueError(
                f"BoardPosition: x must be between zero and two. Received: {x}")

        if not (0 <= y <= 2):
            raise ValueError(
                f"BoardPosition: y must be between 0 and two. Received: {y}")

        super().__init__(x, y)
