"""
Вправа 2: setup / teardown для «ресурсу».

Мета: зімітувати з'єднання, яке відкривається на setup
і закривається на teardown. Без реальної мережі — звичайний dict.

Замініть pass / TODO на правильний код.

Запуск: pytest exercise_2_cleanup.py -v
"""

import pytest


@pytest.fixture
def connection():
    """
    Фікстура має:
      1. створити conn = {"status": "open", "queries": []}  (setup)
      2. віддати conn через yield
      3. після тесту поставити conn["status"] = "closed"  (teardown)
    """
    # TODO: setup — conn = {"status": "open", "queries": []}
    # TODO: yield conn
    # TODO: teardown — conn["status"] = "closed"
    pass


def test_connection_open(connection):
    """Усередині тесту з'єднання відкрите."""
    # TODO: замініть pass на: assert connection["status"] == "open"
    pass


def test_no_queries_initially(connection):
    """Спочатку запитів немає."""
    # TODO: замініть pass на: assert connection["queries"] == []
    pass


def test_add_query(connection):
    """Додаємо «запит» до ресурсу."""
    connection["queries"].append("SELECT 1")
    # TODO: замініть pass на: assert len(connection["queries"]) == 1
    pass


def test_queries_reset(connection):
    """Кожен тест отримує свіже з'єднання (запити скинуті)."""
    # TODO: замініть pass на: assert connection["queries"] == []
    pass
