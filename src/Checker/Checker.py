from enum import Enum


class CheckerType(Enum):
    O = 0
    X = 1


class Checker():

    match_type = None

    def __init__(self, match_type: type[CheckerType]) -> None:

        if not isinstance(match_type, CheckerType):
            raise TypeError("Argument must be of type CheckerType")

        self.match_type = match_type

    def get_type(self):
        return self.match_type
