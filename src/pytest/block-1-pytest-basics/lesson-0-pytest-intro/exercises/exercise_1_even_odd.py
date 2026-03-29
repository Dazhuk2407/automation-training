"""
Вправа 1: Тестування парних/непарних чисел

Функції is_even та is_odd вже написані.
Ваше завдання — дописати тести.

Запуск: pytest exercise_1_even_odd.py -v
"""


# --- Готові функції (НЕ змінюйте!) ---

def is_even(n):
    """Повертає True якщо число парне."""
    return n % 2 == 0


def is_odd(n):
    """Повертає True якщо число непарне."""
    return n % 2 != 0


# --- Ваші тести (допишіть замість pass) ---

def test_two_is_even():
    """Перевірити що 2 — парне число."""
    # TODO: замініть pass на: assert is_even(2) is True
    pass


def test_three_is_not_even():
    """Перевірити що 3 — не парне число."""
    # TODO: замініть pass на: assert is_even(3) is False
    pass


def test_zero_is_even():
    """Перевірити що 0 — парне число."""
    # TODO: замініть pass на: assert is_even(0) is True
    pass


def test_seven_is_odd():
    """Перевірити що 7 — непарне число."""
    # TODO: замініть pass на: assert is_odd(7) is True
    pass


def test_four_is_not_odd():
    """Перевірити що 4 — не непарне число."""
    # TODO: замініть pass на: assert is_odd(4) is False
    pass