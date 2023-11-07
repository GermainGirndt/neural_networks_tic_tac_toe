import pytest
from src.Match.Match import Match, MatchType


def test_create_match_with_no_arguments_throws_error():
    with pytest.raises(TypeError):
        Match()


def test_can_create_match_with_O():
    match = Match(MatchType.O)
    assert match is not None


def test_can_create_match_with_X():
    match = Match(MatchType.O)
    assert match is not None


def test_create_match_with_string_throws_error():
    with pytest.raises(TypeError):
        Match("string")


def test_create_match_with_number_throws_error():
    with pytest.raises(TypeError):
        Match(1)


def test_get_type_for_match_with_O_returns_O():
    match = Match(MatchType.O)
    assert match.get_type() == MatchType.O


def test_get_type_for_match_with_X_returns_X():
    match = Match(MatchType.X)
    assert match.get_type() == MatchType.X
