"""Tests for even or odd code kata"""
import pytest


PARAMS_TABLE = [
    (22, "Even"),
    (246, "Even"),
    (216, "Even"),
    (777, "Odd"),
    (345, "Odd"),
    (221, "Odd"),
]


@pytest.mark.parametrize("n, result", PARAMS_TABLE)
def test_even_or_odd(n, result):
    """Testing even or odd function"""
    from even_or_odd import even_or_odd_func
    assert even_or_odd_func(n) == result
