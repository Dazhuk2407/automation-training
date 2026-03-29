"""
Вправа 3: Вкладені цикли та enumerate.
Запуск: pytest exercise_3_nested.py -v
"""


def test_flatten():
    """Сплощити вкладений список."""
    nested = [[1, 2], [3, 4], [5]]
    # TODO: замініть pass на:
    #   flat = []
    #   for sublist in nested:
    #       for item in sublist:
    #           flat.append(item)
    #   assert flat == [1, 2, 3, 4, 5]
    pass


def test_enumerate_errors():
    """Знайти індекси HTTP помилок (>= 400)."""
    codes = [200, 200, 404, 200, 500]
    # TODO: замініть pass на:
    #   error_indices = []
    #   for i, code in enumerate(codes):
    #       if code >= 400:
    #           error_indices.append(i)
    #   assert error_indices == [2, 4]
    pass


def test_check_all_fields():
    """Перевірити що кожен user має всі required поля."""
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    required = ["id", "name"]
    # TODO: замініть pass на:
    #   for user in users:
    #       for field in required:
    #           assert field in user
    pass