import pytest


@pytest.mark.parametrize("input,expected", [(1, 2), (3, 4), (5, 6)])
def test_increment(input, expected):
    assert input + 1 == expected
