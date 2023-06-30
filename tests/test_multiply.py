import pytest
from src.calculator import multiply


def test_multiply():
    result = multiply(3, 4)
    assert result == 12


def test_multiply_string():
    with pytest.raises(TypeError):
        multiply("string", 4)
