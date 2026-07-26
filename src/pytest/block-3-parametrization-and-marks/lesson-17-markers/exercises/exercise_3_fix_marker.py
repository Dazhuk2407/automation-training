"""
Вправа 3: Виправте баг.

Маркери тут ПРАВИЛЬНІ та зареєстровані — файл збирається без помилок.
Проблема у ЛОГІЦІ одного тесту: його assert падає.

Крок 1: Запустіть файл — рівно один тест падає.
Крок 2: Прочитайте вивід pytest — що саме не збіглося?
Крок 3: Виправте значення так, щоб assert проходив.
Крок 4: Заповніть блок ВІДПОВІДЬ.

Запуск: pytest exercise_3_fix_marker.py -v
"""

import pytest


@pytest.mark.smoke
def test_status_ok():
    """Цей тест проходить."""
    status_code = 200
    assert status_code == 200


@pytest.mark.api
def test_user_count():
    """Цей тест ПАДАЄ — виправте значення expected або users."""
    users = ["alice", "bob", "carol"]
    expected = 2
    # TODO: тут баг у логіці — виправте так, щоб assert проходив
    assert len(users) == expected


@pytest.mark.critical
def test_order_total():
    """Цей тест проходить."""
    total = 50 + 50
    assert total == 100


# ВІДПОВІДЬ:
# Який тест падав: _______________
# Що показав pytest (assert ... == ...): _______________
# Я виправив: _______________
