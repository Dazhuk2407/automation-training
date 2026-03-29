"""
Вправа 3: Практичні сценарії.
Запуск: pytest exercise_3_practical.py -v
"""


def test_generate_ids():
    """range для генерації ID від 1 до 5."""
    # TODO: замініть pass на:
    #   ids = list(range(1, 6))
    #   assert ids == [1, 2, 3, 4, 5]
    pass


def test_find_error_indices():
    """enumerate для пошуку індексів помилкових кодів."""
    codes = [200, 200, 404, 200, 500]
    # TODO: замініть pass на:
    #   errors = [i for i, code in enumerate(codes) if code >= 400]
    #   assert errors == [2, 4]
    pass


def test_build_users():
    """zip для побудови списку словників."""
    names = ["Alice", "Bob"]
    roles = ["admin", "user"]
    # TODO: замініть pass на:
    #   users = [{"name": n, "role": r} for n, r in zip(names, roles)]
    #   assert users[0] == {"name": "Alice", "role": "admin"}
    #   assert len(users) == 2
    pass