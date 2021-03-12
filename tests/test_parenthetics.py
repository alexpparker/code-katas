import pytest

PARAMS_TABLE = [
    ("()()()", 0),
    (")))(((", -1),
    (")()()(", -1),
    ("()", 0),
    ("((())())", 0),
    ("(()(", 1)
]


@pytest.mark.parametrize("parens, result", PARAMS_TABLE)
def test_parens(parens, result):
    from proper_parens import assessor
    assert assessor(parens) == result
