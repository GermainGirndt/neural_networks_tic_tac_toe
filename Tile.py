from Match import Match


class Tile():

    match = None

    def __init__(self) -> None:
        return

    def put_match(self, match: type[Match]) -> None:
        self.match = match
        return

    def get_match(self) -> type[Match]:
        return self.match
