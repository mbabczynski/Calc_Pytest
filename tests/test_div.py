import pytest
from src.calculator import divide


def test_divide():
    result = divide(4, 2)
    assert result == 2


def test_divide_string():
    with pytest.raises(TypeError):
        divide("string", 4)
