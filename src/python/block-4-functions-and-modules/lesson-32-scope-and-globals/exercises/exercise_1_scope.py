"""Вправа 1: Scope. Запуск: pytest exercise_1_scope.py -v"""


def increment(n):
    """Чиста функція — повертає n + 1."""
    # TODO: return n + 1
    pass

def add_tax(price, rate):
    """Чиста функція — ціна з податком."""
    # TODO: return price * (1 + rate)
    pass

def test_increment():
    # TODO: assert increment(0) == 1 та assert increment(5) == 6
    pass

def test_increment_pure():
    """Два виклики з однаковим аргументом → однаковий результат."""
    # TODO: assert increment(10) == increment(10)
    pass

def test_add_tax():
    # TODO: assert add_tax(100, 0.2) == 120.0
    pass

def test_local_does_not_leak():
    """Змінна всередині функції не видна зовні."""
    def inner():
        secret = 42
        return secret
    # TODO:
    #   assert inner() == 42
    #   # secret не існує тут — це перевіряється відсутністю NameError
    pass