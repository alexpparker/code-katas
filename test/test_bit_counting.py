"""Tests for find bit counting code kata"""
import pytest

PARAMS_TABLE = [
    (1, 1),
    (54, 4),
    (5, 2),
    (9999, 8),
    (5000, 5)
]


@pytest.mark.parametrize("number, result", PARAMS_TABLE)
def test_bit_counting(number, result):
    """Testing find the bit counting kata"""
    from bit_counting import count_bits
    assert count_bits(number) == result
