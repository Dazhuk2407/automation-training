"""
Приклад 3: yield-фікстури для ресурсів.

Імітуємо «з'єднання» звичайним dict (без реальної мережі),
а для файлу використовуємо вбудовану фікстуру tmp_path.

Запуск: pytest example_3_resource.py -v
"""

import pytest


@pytest.fixture
def connection():
    """Імітація ресурсу: «відкрити» на setup, «закрити» на teardown."""
    conn = {"status": "open", "queries": []}   # setup — відкрили
    yield conn                                   # тест виконує «запити»
    conn["status"] = "closed"                    # teardown — закрили


def test_connection_is_open(connection):
    """Усередині тесту з'єднання відкрите."""
    assert connection["status"] == "open"


def test_can_run_queries(connection):
    """Можна «виконувати запити» через ресурс."""
    connection["queries"].append("SELECT 1")
    connection["queries"].append("SELECT 2")
    assert len(connection["queries"]) == 2
    assert connection["status"] == "open"


@pytest.fixture
def prepared_users():
    """Тест-дані: створити перед тестом, очистити після."""
    users = ["alice", "bob"]     # setup — підготували дані
    yield users
    users.clear()                # teardown — прибрали


def test_users_prepared(prepared_users):
    """Тест бачить підготовлені дані."""
    assert prepared_users == ["alice", "bob"]
    assert "alice" in prepared_users


def test_temp_file_with_tmp_path(tmp_path):
    """
    Вбудована фікстура tmp_path дає тимчасову директорію
    і сама прибирає її після тесту — реальний файл без ручного teardown.
    """
    file = tmp_path / "data.txt"
    file.write_text("hello", encoding="utf-8")
    assert file.read_text(encoding="utf-8") == "hello"
    assert file.exists()
