# Exercises for Pytest Basics

import pytest


def is_even(number):
    """Check if number is even"""
    return number % 2 == 0


def is_prime(number):
    """Check if number is prime"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


class TestEvenNumbers:
    """Test even number detection"""

    def test_even_number_2(self):
        """TODO: Test that 2 is even"""
        pass

    def test_even_number_10(self):
        """TODO: Test that 10 is even"""
        pass

    def test_odd_number_3(self):
        """TODO: Test that 3 is not even"""
        pass


class TestPrimeNumbers:
    """Test prime number detection"""

    def test_prime_number_2(self):
        """TODO: Test that 2 is prime"""
        pass

    def test_prime_number_13(self):
        """TODO: Test that 13 is prime"""
        pass

    def test_not_prime_number_4(self):
        """TODO: Test that 4 is not prime"""
        pass

