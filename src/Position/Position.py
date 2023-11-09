class Position:

    x = -1
    y = -1

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.validate_position()

    def validate_position(self):
        if type(self.x) != int:
            raise TypeError(
                f"Position: x must be an integer. Received: {type(self.x)} - {self.x}")

        if type(self.y) != int:
            raise TypeError(
                f"Position: y must be an integer. Received: {type(self.y)} - {self.y}")

        if self.x < 0:
            raise ValueError(
                f"Position: x must be greater than or equal to zero. Received: {self.x}")

        if self.y < 0:
            raise ValueError(
                f"Position: y must be greater than or equal to zero. Received: {self.y}")
