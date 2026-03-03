# Приклади базових тестів з Pytest

import pytest


def add(a, b):
    """Simple addition function"""
    return a + b


def subtract(a, b):
    """Simple subtraction function"""
    return a - b


def divide(a, b):
    """Simple division function with error handling"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Simple test functions
def test_add():
    """Test addition"""
    result = add(2, 3)
    assert result == 5


def test_subtract():
    """Test subtraction"""
    result = subtract(10, 4)
    assert result == 6


def test_divide():
    """Test division"""
    result = divide(10, 2)
    assert result == 5.0


def test_divide_by_zero():
    """Test division by zero raises error"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# Class-based tests
class TestMath:
    """Test class for math operations"""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-2, -3) == -5

    def test_subtract_positive(self):
        assert subtract(10, 5) == 5


# Test with setup and teardown
class TestWithSetup:
    """Tests with setup and teardown"""

    def setup_method(self):
        """Run before each test method"""
        self.value = 10

    def teardown_method(self):
        """Run after each test method"""
        self.value = None

    def test_value_exists(self):
        assert self.value == 10

    def test_value_type(self):
        assert isinstance(self.value, int)

