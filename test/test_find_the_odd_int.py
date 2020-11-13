"""Tests for find the odd int code kata"""
import pytest

PARAMS_TABLE = [
    ([1, 1, 2, 3, 3, 4, 4], 2),
    ([67, -21, 67, 99, -21, 54, 99], 54),
    ([5], 5),
]


@pytest.mark.parametrize("seq, result", PARAMS_TABLE)
def test_find_the_odd_int(seq, result):
    """Testing find the odd int kata"""
    from find_the_odd_int import find_the_odd_int_func
    assert find_the_odd_int_func(seq) == result
