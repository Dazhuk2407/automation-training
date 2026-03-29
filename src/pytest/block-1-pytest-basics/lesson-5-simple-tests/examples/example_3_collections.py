"""
Приклад 3: Тести для колекцій (list, dict, set, tuple).

Запуск: pytest example_3_collections.py -v
"""


# --- Списки (list) ---

def test_list_basics():
    """Довжина, індекси, слайси."""
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert numbers[0] == 1
    assert numbers[-1] == 5
    assert numbers[1:3] == [2, 3]


def test_list_membership():
    """Належність елемента до списку."""
    fruits = ["apple", "banana", "cherry"]
    assert "apple" in fruits
    assert "orange" not in fruits


def test_list_sorting():
    """Сортування (sorted повертає новий список)."""
    assert sorted([3, 1, 2]) == [1, 2, 3]
    assert sorted([3, 1, 2], reverse=True) == [3, 2, 1]


# --- Словники (dict) ---

def test_dict_access():
    """Доступ до значень словника."""
    user = {"name": "Alice", "age": 25}
    assert user["name"] == "Alice"
    assert user.get("phone") is None


def test_dict_keys():
    """Перевірка наявності ключів."""
    config = {"debug": True, "port": 8080}
    assert "debug" in config
    assert "host" not in config


# --- Множини (set) ---

def test_set_removes_duplicates():
    """Множина автоматично прибирає дублікати."""
    unique = {1, 2, 3, 3, 4, 4}
    assert len(unique) == 4
    assert 3 in unique


# --- Кортежі (tuple) ---

def test_tuple_basics():
    """Кортеж — незмінна колекція."""
    point = (10, 20)
    assert point[0] == 10
    assert point[1] == 20
    assert len(point) == 2