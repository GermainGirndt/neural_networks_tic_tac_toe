class Position:

    x = -1
    y = -1

    def __init__(self, x, y) -> None:

        if type(x) != int:
            raise TypeError(
                f"Position: x must be an integer. Received: {type(x)} - {x}")

        if type(y) != int:
            raise TypeError(
                f"Position: y must be an integer. Received: {type(y)} - {y}")

        if x < 0:
            raise ValueError(
                f"Position: x must be greater than or equal to zero. Received: {x}")

        if y < 0:
            raise ValueError(
                f"Position: y must be greater than or equal to zero. Received: {y}")

        self.x = x
        self.y = y
