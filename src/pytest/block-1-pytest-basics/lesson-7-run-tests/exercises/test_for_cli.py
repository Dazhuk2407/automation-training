"""
Тестовий файл для практики CLI-команд.

Використовуйте цей файл для вправ з Lesson 7.
Запускайте різними способами і порівнюйте вивід.
"""

import pytest


# --- Прості тести ---

def test_addition():
    """Тест додавання."""
    assert 2 + 3 == 5


def test_subtraction():
    """Тест віднімання."""
    assert 10 - 4 == 6


def test_string_contains():
    """Тест вмісту рядка."""
    assert "test" in "pytest"


def test_list_sorted():
    """Тест сортування списку."""
    assert sorted([3, 1, 2]) == [1, 2, 3]


# --- Тест з print() (видно тільки з -s) ---

def test_with_print():
    """Тест з print — запустіть з -s щоб побачити."""
    print(">>> Цей текст видно тільки з pytest -s")
    assert True


# --- Тестовий клас (для практики шляхів) ---

class TestStrings:
    """Тести для рядків."""

    def test_upper(self):
        assert "hello".upper() == "HELLO"

    def test_lower(self):
        assert "WORLD".lower() == "world"

    def test_strip(self):
        assert "  spaces  ".strip() == "spaces"


# --- Повільний тест (для -k "not slow") ---

def test_slow_operation():
    """Повільний тест — для практики фільтрації."""
    import time
    time.sleep(0.05)
    assert True


# --- Падаючий тест (розкоментуйте для практики -x) ---

# def test_intentional_fail():
#     """Розкоментуйте для практики -x та --maxfail."""
#     assert 5 == 10