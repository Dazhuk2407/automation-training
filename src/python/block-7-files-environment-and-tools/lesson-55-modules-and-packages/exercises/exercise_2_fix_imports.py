"""Вправа 2: виправ помилку. Запуск: pytest exercise_2_fix_imports.py -v

Один тест падає. Знайди баг (позначено # BUG:) і виправ його.
Після виправлення всі тести мають бути зеленими.

Уяви, що це модуль з утилітами, який реекспортує функції.
"""


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


# "Реекспорт" — публічний список функцій модуля
def get_public_api():
    # BUG: модуль надає ДВІ функції (add і multiply), а в списку лише add
    return ["add"]


def module_mode(name):
    return "script" if name == "__main__" else "imported"


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 4) == 8


def test_public_api_has_both():
    assert set(get_public_api()) == {"add", "multiply"}


def test_mode_imported():
    assert module_mode("utils") == "imported"
