"""Tests for create phone number code kata"""
import pytest

PARAMS_TABLE = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "(111) 111-1111"),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"),
    ([0, 2, 3, 0, 5, 6, 0, 8, 9, 0], "(023) 056-0890"),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "(000) 000-0000")
]


@pytest.mark.parametrize("lst, phone_number", PARAMS_TABLE)
def test_create_phone_number(lst, phone_number):
    """Testing create phone number kata"""
    from create_phone_number import create_phone_number_func
    assert create_phone_number_func(lst) == phone_number
