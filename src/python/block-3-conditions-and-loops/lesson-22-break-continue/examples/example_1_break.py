"""
Приклад 1: break — вихід з циклу.
Запуск: pytest example_1_break.py -v
"""


def test_find_first_error():
    """break на першій помилці."""
    codes = [200, 200, 404, 500, 200]
    first_error = None
    for code in codes:
        if code >= 400:
            first_error = code
            break
    assert first_error == 404


def test_break_stops_loop():
    """Після break решта не виконується."""
    processed = []
    for i in range(10):
        if i == 3:
            break
        processed.append(i)
    assert processed == [0, 1, 2]


def test_search_with_break():
    """Пошук користувача за ім'ям."""
    users = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
    found = None
    for user in users:
        if user["name"] == "Bob":
            found = user
            break
    assert found == {"name": "Bob"}


def test_break_in_while():
    """break у while циклі."""
    values = [1, 3, 5, 8, 2, 4]
    first_even = None
    i = 0
    while i < len(values):
        if values[i] % 2 == 0:
            first_even = values[i]
            break
        i += 1
    assert first_even == 8