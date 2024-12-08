import pytest

from main import get_even_numbers, get_odd_numbers


@pytest.mark.parametrize(
    "input_numbers, expected_output",
    [
        ((1, 2, 3, 4, 5, 6), (1, 3, 5)),
        ((2, 4, 6, 8), ()),
        ((1, 3, 5, 7), (1, 3, 5, 7)),
        ((), ()),
        ((0, 2, 4), ()),
        ((-3, -2, -1, 0, 1, 2, 3), (-3, -1, 1, 3)),
    ],
)
def test_get_odd_numbers(input_numbers, expected_output):
    assert get_odd_numbers(input_numbers) == expected_output


@pytest.mark.parametrize(
    "input_numbers, expected_output",
    [
        ((1, 2, 3, 4, 5, 6), (2, 4, 6)),
        ((2, 4, 6, 8), (2, 4, 6, 8)),
        ((1, 3, 5, 7), ()),
        ((), ()),
        ((0, 2, 4), (0, 2, 4)),
        ((-3, -2, -1, 0, 1, 2, 3), (-2, 0, 2)),
    ],
)
def test_get_even_numbers(input_numbers, expected_output):
    assert get_even_numbers(input_numbers) == expected_output
