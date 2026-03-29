"""
Приклад 2: Методи списків — зміна, додавання, видалення, сортування.

Запуск: pytest example_2_methods.py -v
"""


def test_append_and_extend():
    """append додає один елемент, extend — кілька."""
    errors = [404]
    errors.append(500)
    assert errors == [404, 500]

    errors.extend([502, 503])
    assert errors == [404, 500, 502, 503]


def test_insert():
    """insert додає елемент за індексом."""
    steps = ["login", "submit"]
    steps.insert(1, "fill_form")
    assert steps == ["login", "fill_form", "submit"]


def test_remove_and_pop():
    """remove видаляє за значенням, pop — за індексом."""
    users = ["Alice", "Bob", "Charlie", "Diana"]

    users.remove("Bob")
    assert users == ["Alice", "Charlie", "Diana"]

    last = users.pop()
    assert last == "Diana"
    assert users == ["Alice", "Charlie"]

    first = users.pop(0)
    assert first == "Alice"
    assert users == ["Charlie"]


def test_sorted_vs_sort():
    """sorted() повертає новий список, .sort() змінює на місці."""
    times = [150, 30, 200, 45]

    # sorted — новий список, оригінал не змінюється
    sorted_times = sorted(times)
    assert sorted_times == [30, 45, 150, 200]
    assert times == [150, 30, 200, 45]  # не змінився

    # sort — змінює на місці, повертає None
    result = times.sort()
    assert result is None
    assert times == [30, 45, 150, 200]  # тепер змінився


def test_count_and_index():
    """count рахує входження, index шукає позицію."""
    codes = [200, 200, 404, 200, 500]
    assert codes.count(200) == 3
    assert codes.index(404) == 2