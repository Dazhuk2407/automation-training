"""
Приклад 3: Best practices та анти-патерни.

Запуск: pytest example_3_best_practices.py -v

Один тест навмисно падає — щоб показати як pytest відображає diff.
"""


# --- Pytest introspection demo ---

def test_dict_diff_demo():
    """Цей тест НАВМИСНО падає — подивіться на diff у виводі pytest."""
    expected = {"name": "Alice", "age": 25, "city": "Kyiv"}
    actual = {"name": "Alice", "age": 30, "city": "Kyiv"}
    assert actual == expected


# --- Правильний стиль ---

def test_good_boolean():
    """Правильно: assert condition, а не assert condition is True."""
    is_active = True
    assert is_active
    assert not False


def test_good_none_check():
    """Правильно: is None / is not None."""
    value = None
    assert value is None

    other = "data"
    assert other is not None


def test_good_isinstance():
    """Правильно: isinstance замість type() == ..."""
    assert isinstance(42, int)
    assert isinstance("text", str)


# --- Message тільки коли потрібен контекст ---

def test_message_useful():
    """Message корисний для складної логіки."""
    users = ["Alice", "Bob"]
    target = "Alice"
    assert target in users, f"User '{target}' should exist in database"


def test_message_unnecessary():
    """Тут message не потрібен — pytest сам покаже diff."""
    assert 2 + 3 == 5