"""
Тестовий файл для аналізу виводу pytest.

Запускайте з різними опціями:
    pytest test_output_practice.py -v
    pytest test_output_practice.py --tb=short
    pytest test_output_practice.py -l
    pytest test_output_practice.py -s
"""

import pytest


# --- PASSED ---

def test_passing_math():
    """Простий тест — пройде."""
    assert 2 + 3 == 5


def test_passing_string():
    """Рядковий тест — пройде."""
    assert "hello".upper() == "HELLO"


# --- FAILED (assert не пройшов) ---

def test_failed_comparison():
    """Assert падає — порівняння чисел."""
    result = 42
    assert result == 100


def test_failed_dict():
    """Assert падає — порівняння словників."""
    expected = {"name": "Alice", "age": 25}
    actual = {"name": "Alice", "age": 30}
    assert actual == expected


# --- ERROR (код зламався до assert) ---

def test_error_zero_division():
    """Помилка в коді — ділення на нуль."""
    result = 10 / 0
    assert result == 5


def test_error_key_missing():
    """Помилка в коді — неіснуючий ключ."""
    config = {"host": "localhost"}
    port = config["port"]
    assert port == 8080


# --- SKIPPED ---

@pytest.mark.skip(reason="Демонстрація SKIPPED")
def test_skipped():
    """Цей тест пропущений."""
    assert True


# --- XFAIL ---

@pytest.mark.xfail(reason="Демонстрація XFAIL")
def test_expected_to_fail():
    """Очікуємо падіння — показує 'x' у виводі."""
    assert 1 == 2


# --- Print ---

def test_with_print():
    """Тест з print() — видно тільки з -s."""
    print(">>> Цей текст видно тільки з pytest -s")
    assert True


# --- Multiple asserts ---

def test_multiple_asserts():
    """Третій assert впаде — четвертий не виконається."""
    assert 1 + 1 == 2
    assert 2 + 2 == 4
    assert 3 + 3 == 5   # ❌ впаде тут
    assert 4 + 4 == 8   # ⛔ не виконається