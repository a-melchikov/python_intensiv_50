import pytest
from exercises.ex5 import pig_latin


@pytest.mark.parametrize(
    "string, expected",
    [
        ("andrey", "andreyway"),
        ("ruby", "ubyray"),
        ("name", "amenay"),
        ("computer", "omputercay"),
        ("how?", "owhay?"),
    ],
)
def test_pig_latin(string, expected):
    assert pig_latin(string) == expected
