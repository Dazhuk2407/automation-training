"""
Вправа 3: Виправте зламаний teardown.

У фікстурі session використано return замість yield.
Через це teardown ніколи не виконується — один тест падає.

Крок 1: Запустіть файл — знайдіть тест, що падає.
Крок 2: Зрозумійте ЧОМУ teardown не спрацював.
Крок 3: Виправте фікстуру.
Крок 4: Заповніть блок ВІДПОВІДЬ.

Запуск: pytest exercise_3_fix_teardown.py -v
"""

import pytest


# Журнал подій — щоб побачити, чи виконався teardown.
events = []


@pytest.fixture
def session():
    """
    ❌ БАГ: return завершує фікстуру, і рядок teardown нижче — мертвий код.
    Через це "teardown" ніколи не потрапляє в events.
    """
    events.append("setup")
    data = {"open": True}
    return data                       # ❌ через return teardown не виконається
    events.append("teardown")         # цей рядок ніколи не запускається


def test_session_open(session):
    """Усередині тесту сесія відкрита."""
    assert session["open"] is True


def test_session_is_dict(session):
    """session має бути словником."""
    assert isinstance(session, dict)


def test_teardown_ran():
    """
    Після попередніх тестів teardown мав виконатись.
    Зараз цей тест ПАДАЄ — бо return не дав виконати teardown.
    """
    assert "teardown" in events


# ВІДПОВІДЬ:
# Причина падіння: _______________
# Що виправив: замінив ______ на ______
# Чому це працює: _______________
