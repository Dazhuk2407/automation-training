"""
Приклад 1: Спільна фікстура з conftest.py.

Фікстура `sample_user` оголошена в examples/conftest.py.
Цей файл використовує її БЕЗ import — pytest сам її знайде.

Запуск: pytest example_1_shared_fixture.py -v
"""


def test_user_name(sample_user):
    """Фікстура приходить з conftest.py як аргумент."""
    assert sample_user["name"] == "Alice"


def test_user_is_admin(sample_user):
    """Той самий conftest-fixture, свіжа копія для цього тесту."""
    assert sample_user["role"] == "admin"


def test_user_has_expected_keys(sample_user):
    """Немає жодного import — і все працює."""
    assert "name" in sample_user
    assert "role" in sample_user
