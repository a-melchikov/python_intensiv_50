import pytest
from exercises.ex4 import hex_output


@pytest.mark.parametrize(
    "hex_num",
    [
        "0x0",
        "0x1",
        "0xA",
        "0xF",
        "0x10",
        "0x100",
        "0xFF",
        "0x123456",
        "123",
        "0xdeadbeef",
    ],
)
def test_hex_output(hex_num):
    assert hex_output(hex_num) == int(hex_num, 16)


if __name__ == "__main__":
    pytest.main()
