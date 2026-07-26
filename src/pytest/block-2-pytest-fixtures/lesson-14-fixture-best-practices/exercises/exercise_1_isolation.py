"""
Вправа 1: Ізоляція фікстур.

Фікстура fresh_inbox вже написана правильно (function-scope, свіжі дані).
Ваше завдання — замінити pass на assert, щоб перевірити, що тести
НЕ впливають один на одного.

Запуск: pytest exercise_1_isolation.py -v
"""

import pytest


@pytest.fixture
def fresh_inbox():
    """Свіжа скринька повідомлень для кожного тесту (function-scope)."""
    return {"messages": []}


def test_inbox_starts_empty():
    """Локальний список порожній на старті. Використайте власний список."""
    inbox = []
    # TODO: замініть pass на: assert inbox == []
    pass


def test_add_one_message(fresh_inbox):
    """Додайте одне повідомлення і перевірте довжину."""
    fresh_inbox["messages"].append("hello")
    # TODO: замініть pass на: assert len(fresh_inbox["messages"]) == 1
    pass


def test_inbox_is_isolated(fresh_inbox):
    """Ізоляція: попередній тест не вплинув — скринька знову порожня."""
    # TODO: замініть pass на: assert fresh_inbox["messages"] == []
    pass


def test_two_messages(fresh_inbox):
    """Додайте два повідомлення і перевірте вміст."""
    fresh_inbox["messages"].append("a")
    fresh_inbox["messages"].append("b")
    # TODO: замініть pass на: assert fresh_inbox["messages"] == ["a", "b"]
    pass


def test_still_isolated(fresh_inbox):
    """Знову свіжа скринька — жодних слідів "a"/"b"."""
    # TODO: замініть pass на: assert "a" not in fresh_inbox["messages"]
    pass
