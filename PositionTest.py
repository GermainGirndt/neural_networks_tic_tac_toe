import pytest
from Position import Position


def test_can_create_position_with_x_and_y_equals_zero():
    position = Position(x=0, y=0)
    assert position is not None


def test_can_create_position_with_x_and_y_equals_one():
    position = Position(x=1, y=1)
    assert position is not None


def test_create_position_with_x_equals_minus_one_and_y_equals_zero_should_throw_error():
    with pytest.raises(ValueError):
        Position(x=-1, y=0)


def test_create_position_with_y_equals_minus_one_and_x_equals_zero_should_throw_error():
    with pytest.raises(ValueError):
        Position(x=0, y=-1)


def test_create_position_with_x_equals_string_and_y_equals_zero_should_throw_error():
    with pytest.raises(TypeError):
        Position(x="invalid_value", y=0)


def test_create_position_with_y_equals_string_and_x_equals_zero_should_throw_error():
    with pytest.raises(TypeError):
        Position(x=0, y="invalid_value")


def test_create_position_with_x_equals_one_point_five_should_throw_error():
    with pytest.raises(TypeError):
        Position(x=1.5, y=0)


def test_create_position_with_y_equals_one_point_five_should_throw_error():
    with pytest.raises(TypeError):
        Position(x=0, y=1.5)
