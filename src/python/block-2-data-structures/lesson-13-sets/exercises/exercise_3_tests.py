"""
Вправа 3: Множини у тестових сценаріях.
Запуск: pytest exercise_3_tests.py -v
"""


def test_required_fields():
    """API повертає всі обов'язкові поля."""
    required = {"id", "name", "email"}
    response = {"id": 1, "name": "Alice", "email": "a@t.com", "avatar": None}
    # TODO: замініть pass на: assert required.issubset(response.keys())
    pass


def test_no_duplicates():
    """ID користувачів унікальні."""
    users = [{"id": 1}, {"id": 2}, {"id": 3}]
    ids = [u["id"] for u in users]
    # TODO: замініть pass на: assert len(ids) == len(set(ids))
    pass


def test_new_features():
    """Нові функції у v2 порівняно з v1."""
    v1 = {"dark_mode", "export"}
    v2 = {"dark_mode", "export", "notifications", "chat"}
    # TODO: замініть pass на:
    #   new = v2 - v1
    #   assert new == {"notifications", "chat"}
    pass


def test_deduplicate():
    """Прибрати дублікати зі списку помилок."""
    errors = ["timeout", "404", "timeout", "500", "timeout"]
    # TODO: замініть pass на:
    #   unique = set(errors)
    #   assert len(unique) == 3
    pass