"""
Приклад 2: Мінімальний scope — бери найвужчий, розширюй лише для дорогих ресурсів.

- Дешеві дані → function-scope (свіжі для кожного тесту).
- Дорогий ресурс (умовне "з'єднання") → session-scope, створюється ОДИН раз
  і використовується як read-only, тому спільний стан безпечний.

Запуск: pytest example_2_minimal_scope.py -v
"""

import pytest


@pytest.fixture
def order_items():
    """Дешево створити → найвужчий scope (function). Свіжий список кожному тесту."""
    return ["book", "pen"]


@pytest.fixture(scope="session")
def db_config():
    """
    Умовно "дорогий" ресурс: створюємо ОДИН раз на сесію.
    Повертаємо read-only конфіг — тести його не мутують, тому scope безпечний.
    """
    # Уявімо, що тут дороге з'єднання; для прикладу — просто незмінний конфіг.
    return {"host": "test-db.local", "port": 5432, "readonly": True}


def test_items_are_fresh_first(order_items):
    """Function-scope: свіжий список."""
    order_items.append("laptop")
    assert order_items == ["book", "pen", "laptop"]


def test_items_are_fresh_second(order_items):
    """Знову свіжий — попередній append не вплинув."""
    assert order_items == ["book", "pen"]


def test_db_config_shared_readonly(db_config):
    """Session-ресурс лише читаємо."""
    assert db_config["host"] == "test-db.local"


def test_db_config_still_intact(db_config):
    """Той самий об'єкт, але ніхто його не змінив — стан стабільний."""
    assert db_config["readonly"] is True
