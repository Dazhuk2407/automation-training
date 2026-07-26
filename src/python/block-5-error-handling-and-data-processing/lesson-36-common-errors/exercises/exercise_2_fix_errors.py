"""Вправа 2: виправ помилку. Запуск: pytest exercise_2_fix_errors.py -v

Деякі тести падають через баг у коді нижче.
Знайди функцію з коментарем # BUG, зрозумій який виняток вона спричиняє,
і виправ її. Після фіксу всі тести мають стати зеленими.
"""


def get_age(user):
    """Повернути вік користувача, або 0 якщо поля немає."""
    # BUG: знайди і виправ — падає з KeyError коли ключа 'age' немає
    return user["age"]


def last_item(items):
    """Повернути останній елемент списку, або None для порожнього."""
    if not items:
        return None
    return items[-1]


def success_rate(passed, total):
    """Відсоток пройдених тестів."""
    if total == 0:
        return 0.0
    return passed / total * 100


def test_get_age_present():
    assert get_age({"name": "Alice", "age": 30}) == 30


def test_get_age_missing():
    assert get_age({"name": "Bob"}) == 0


def test_last_item():
    assert last_item([1, 2, 3]) == 3
    assert last_item([]) is None


def test_success_rate():
    assert success_rate(3, 4) == 75.0
    assert success_rate(0, 0) == 0.0
