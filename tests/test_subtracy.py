import pytest
from src.calculator import subtract


def test_subtract():
    result = subtract(5, 2)
    assert result == 3


def test_subtract_string():
    with pytest.raises(TypeError):
        subtract("string", 4)
