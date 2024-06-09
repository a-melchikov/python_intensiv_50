import pytest
from exercises.ex3 import float_int_int


@pytest.mark.parametrize(
    "float_, before_, after_, expected",
    [
        (123.456, 5, 5, 123.456),
        (123456.789, 3, 2, 456.78),
        (123.456789, 3, 3, 123.456),
        (123.456, 0, 3, 0.456),
        (123.456, 3, 0, 123.0),
        (123.0, 3, 2, 123.0),
        (12.345, 5, 3, 12.345),
        (12.3, 3, 5, 12.3),
    ],
)
def test_float_int_int(float_, before_, after_, expected):
    assert float_int_int(float_, before_, after_) == expected


if __name__ == "__main__":
    pytest.main()
