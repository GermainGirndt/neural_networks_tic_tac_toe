from src.Board.BoardPosition import BoardPosition
from src.Tile.Tile import Tile


class Board():

    tiles = None

    def __init__(self) -> None:
        self.tiles = []

        for row in range(3):
            row_tiles = []
            for column in range(3):
                column_tile = Tile(BoardPosition(row, column))
                row_tiles.append(column_tile)
            self.tiles.append(row_tiles)

    def get_tiles(self) -> list:
        return self.tiles

    def get_tile(self, board_position: type[BoardPosition]) -> type[Tile]:
        return self.tiles[board_position.x][board_position.y]
