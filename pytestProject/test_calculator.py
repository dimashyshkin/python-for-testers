import pytest

from calculator import add_numbers


@pytest.mark.positive
@pytest.mark.parametrize("num1, num2, expected", [(3, 5, 8), (5, -3, 2), (-2, -3, -5)])
def test_add_numbers(num1, num2, expected):
    result = add_numbers(num1, num2)
    assert result == expected


@pytest.mark.negative
def test_add_positive_negative():
    result = add_numbers(5, -3)
    assert result == 2


@pytest.mark.negative
def test_add_two_negatives():
    result = add_numbers(-2, -3)
    assert result == -5
