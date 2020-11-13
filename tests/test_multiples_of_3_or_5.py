"""Tests for multiples of 3 or 5 code kata"""
import pytest

PARAMS_TABLE = [
    (4, 3),
    (10, 23),
    (13, 45),
    (0, 0),
    (3, 0),
    (6, 8)
]


@pytest.mark.parametrize("n, result", PARAMS_TABLE)
def test_multiples_of_3_or_5(n, result):
    """Testing the multiples of 3 or 5 kata"""
    from multiples_of_3_or_5 import multiples_of_3_or_5_func
    assert multiples_of_3_or_5_func(n) == result
