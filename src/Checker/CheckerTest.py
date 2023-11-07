import pytest
from src.Checker.Checker import Checker, CheckerType


def test_create_match_with_no_arguments_throws_error():
    with pytest.raises(TypeError):
        Checker()


def test_can_create_match_with_O():
    checker = Checker(CheckerType.O)
    assert checker is not None


def test_can_create_match_with_X():
    checker = Checker(CheckerType.O)
    assert checker is not None


def test_create_match_with_string_throws_error():
    with pytest.raises(TypeError):
        Checker("string")


def test_create_match_with_number_throws_error():
    with pytest.raises(TypeError):
        Checker(1)


def test_get_type_for_match_with_O_returns_O():
    checker = Checker(CheckerType.O)
    assert checker.get_type() == CheckerType.O


def test_get_type_for_match_with_X_returns_X():
    checker = Checker(CheckerType.X)
    assert checker.get_type() == CheckerType.X
