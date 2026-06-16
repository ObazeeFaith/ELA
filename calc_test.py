from app.math_operations import add, subtract, multiply, divide
import pytest
def test_add():
    a = 5
    b = 3
    expected = 8
    result = add(a,b )
    assert result == expected

@pytest.mark.parametrize("input_number, expected_result", [
    (2, True),
    (9, False)
])
def test_prime(input_number, expected_result):
    assert test_prime(input_number) == expected_result