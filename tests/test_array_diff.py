"""Tests for array.diff code kata"""
import pytest

PARAMS_TABLE = [
    ([1, 2], [1], [2]),
    ([22, 2, 0, 22], [22, 2, 0], []),
    ([70, 60], [1, 2, 3, 4], [70, 60])
]


@pytest.mark.parametrize("a, b, result", PARAMS_TABLE)
def test_array_diff(a, b, result):
    """Testing array diff kata"""
    from array_diff import array_diff_func
    assert array_diff_func(a, b) == result
