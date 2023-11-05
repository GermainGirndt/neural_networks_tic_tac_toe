import pytest
from BoardPosition import BoardPosition


def test_can_create_position_with_x_and_y_equals_zero():
    position = BoardPosition(x=0, y=0)
    assert position is not None


def test_create_position_with_x_equals_3_should_throw_an_error():
    with pytest.raises(ValueError):
        BoardPosition(x=3, y=0)


def test_create_position_with_y_equals_3_should_throw_an_error():
    with pytest.raises(ValueError):
        BoardPosition(x=0, y=3)
