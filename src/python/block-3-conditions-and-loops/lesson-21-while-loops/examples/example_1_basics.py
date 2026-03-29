"""
Приклад 1: Базовий while.
Запуск: pytest example_1_basics.py -v
"""


def test_counter():
    """Лічильник через while."""
    count = 0
    while count < 5:
        count += 1
    assert count == 5


def test_accumulator():
    """Накопичення суми."""
    numbers = [10, 20, 30, 40]
    total = 0
    index = 0
    while index < len(numbers):
        total += numbers[index]
        index += 1
    assert total == 100


def test_collect_while():
    """Збір результатів поки умова True."""
    results = []
    n = 1
    while n <= 32:
        results.append(n)
        n *= 2
    assert results == [1, 2, 4, 8, 16, 32]


def test_countdown():
    """Зворотний відлік."""
    steps = []
    n = 5
    while n > 0:
        steps.append(n)
        n -= 1
    assert steps == [5, 4, 3, 2, 1]