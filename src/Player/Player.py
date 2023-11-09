from src.Checker.Checker import Checker, CheckerType
from src.Board.BoardPosition import BoardPosition
from src.Move.Move import Move


class Player():

    checker_type: type[CheckerType] = None

    def __init__(self, checker_type: type[CheckerType]):
        self.checker_type = checker_type

    def has_same_checker_type(self, player):

        if not isinstance(player, Player):
            raise TypeError(
                "Method has_same_checker_type only accepts Player type")

        return self.checker_type == player.checker_type

    def execute(self, move: type[Move]):

        self.validate_move(move)
        move.execute()

    def validate_move(self, move: type[Move]):

        if not isinstance(move, Move):
            raise TypeError(
                "Method validate_move only accepts Move type")

        if (self.checker_type != move.checker.get_type()):
            raise TypeError("Player and Move checker types must be the same")
