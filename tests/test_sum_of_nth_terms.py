"""Tests for sum of nth terms kata"""
import pytest
from sum_of_nth_terms import series_sum

PARAMS_TABLE = [
    (1, "1.00"),
    (2, "1.25"),
    (3, "1.39")
]

@pytest.mark.parametrize("n, result", PARAMS_TABLE)
def test_series_sum(n, result):
    assert series_sum(n) == result
