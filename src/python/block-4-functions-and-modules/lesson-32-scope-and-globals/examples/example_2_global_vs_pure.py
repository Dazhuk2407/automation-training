"""Приклад 2: Global vs pure functions. Запуск: pytest example_2_global_vs_pure.py -v"""


def add_tax_pure(price, rate):
    """✅ Pure function — легко тестувати."""
    return price * (1 + rate)

def increment(counter):
    """✅ Повертає нове значення замість зміни global."""
    return counter + 1

def test_pure_tax():
    assert add_tax_pure(100, 0.2) == 120.0
    assert add_tax_pure(200, 0.5) == 300.0

def test_increment():
    count = 0
    count = increment(count)
    count = increment(count)
    assert count == 2

def test_pure_is_predictable():
    """Однакові аргументи → однаковий результат."""
    assert add_tax_pure(100, 0.2) == add_tax_pure(100, 0.2)