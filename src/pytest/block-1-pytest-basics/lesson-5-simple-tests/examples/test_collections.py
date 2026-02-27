"""
Lesson 5: Example 3 - Testing Collections (Lists, Dicts, Sets)
"""


def test_list_basics():
    """Базові тести списків."""
    numbers = [1, 2, 3, 4, 5]

    # Довжина
    assert len(numbers) == 5

    # Індекс
    assert numbers[0] == 1
    assert numbers[4] == 5
    assert numbers[-1] == 5

    # Слайсинг
    assert numbers[1:3] == [2, 3]
    assert numbers[:2] == [1, 2]
    assert numbers[2:] == [3, 4, 5]


def test_list_membership():
    """Тест належності елементів у список."""
    fruits = ["apple", "banana", "cherry"]

    assert "apple" in fruits
    assert "banana" in fruits
    assert "orange" not in fruits


def test_list_modification():
    """Тест модифікації списків."""
    numbers = [1, 2, 3]

    # Append
    numbers.append(4)
    assert numbers == [1, 2, 3, 4]

    # Remove
    numbers.remove(2)
    assert numbers == [1, 3, 4]

    # Pop
    last = numbers.pop()
    assert last == 4
    assert numbers == [1, 3]


def test_list_sorting():
    """Тест сортування списків."""
    unsorted = [3, 1, 4, 1, 5, 9, 2, 6]

    # Ascending
    sorted_asc = sorted(unsorted)
    assert sorted_asc == [1, 1, 2, 3, 4, 5, 6, 9]

    # Descending
    sorted_desc = sorted(unsorted, reverse=True)
    assert sorted_desc == [9, 6, 5, 4, 3, 2, 1, 1]


def test_dictionary_basics():
    """Базові тести словників."""
    user = {"name": "Alice", "age": 25, "city": "Kyiv"}

    # Доступ
    assert user["name"] == "Alice"
    assert user["age"] == 25

    # Довжина
    assert len(user) == 3


def test_dictionary_keys_values():
    """Тест ключів та значень словника."""
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

    # Keys
    assert "Alice" in scores
    assert "David" not in scores

    # Values
    assert 95 in scores.values()
    assert max(scores.values()) == 95
    assert min(scores.values()) == 87


def test_set_basics():
    """Базові тести множин."""
    unique = {1, 2, 3, 3, 4, 4, 5}

    # Дублікати видалені
    assert len(unique) == 5

    # Membership
    assert 3 in unique
    assert 6 not in unique


def test_empty_collections():
    """Тест порожніх колекцій."""
    empty_list = []
    empty_dict = {}
    empty_set = set()

    assert len(empty_list) == 0
    assert len(empty_dict) == 0
    assert len(empty_set) == 0

    # Порожні колекції = False
    assert not empty_list
    assert not empty_dict
    assert not empty_set

