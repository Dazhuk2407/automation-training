"""
Приклад 2: Runtime помилки (ERROR, а не FAILED).

Запуск: pytest example_2_runtime_errors.py -v
Результат: 3 errors — код зламався ДО assert.

Спробуйте різні рівні traceback:
    pytest example_2_runtime_errors.py --tb=short
    pytest example_2_runtime_errors.py --tb=no
    pytest example_2_runtime_errors.py -l
"""


def test_zero_division():
    """ZeroDivisionError — ділення на нуль."""
    result = 10 / 0
    assert result == 5


def test_key_error():
    """KeyError — неіснуючий ключ словника."""
    user = {"name": "Alice"}
    email = user["email"]
    assert email == "alice@example.com"


def test_type_error():
    """TypeError — додавання рядка до числа."""
    result = "hello" + 5
    assert result == "hello5"