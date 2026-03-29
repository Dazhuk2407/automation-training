"""
Вправа 5: Розуміння pytest assert introspection.

Крок 1: Запустіть файл — один тест навмисно падає.
Крок 2: Прочитайте вивід pytest — що саме відрізняється?
Крок 3: Заповніть коментар ВІДПОВІДЬ.
Крок 4: Виправте тест щоб він проходив.

Запуск: pytest exercise_5_introspection.py -v
"""


def test_dict_comparison():
    """Цей тест падає — знайдіть різницю і виправте."""
    expected = {"name": "Alice", "age": 25, "role": "admin"}
    actual = {"name": "Alice", "age": 25, "role": "user"}
    # TODO: Виправте actual або expected щоб тест проходив
    assert actual == expected


def test_list_comparison():
    """Цей тест працює правильно."""
    assert sorted([3, 1, 2]) == [1, 2, 3]


# ВІДПОВІДЬ:
# У test_dict_comparison різниця в: _______________
# pytest показав: _______________
# Я виправив: _______________