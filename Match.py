from enum import Enum


class MatchType(Enum):
    O = 0
    X = 1


class Match():

    match_type = None

    def __init__(self, match_type: type[MatchType]) -> None:

        if not isinstance(match_type, MatchType):
            raise TypeError("Argument must be of type MatchType")

        self.match_type = match_type

    def get_type(self):
        return self.match_type
