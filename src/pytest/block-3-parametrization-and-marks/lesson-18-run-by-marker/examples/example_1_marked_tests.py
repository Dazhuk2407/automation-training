"""
Приклад 1: Реальні тести з маркерами — «матеріал» для відбору через -m.

Тут немає нічого складного: усі тести проходять. Мета файлу — показати
набір тестів із різними маркерами, на якому зручно тренувати команди:

    pytest example_1_marked_tests.py -m smoke -v
    pytest example_1_marked_tests.py -m "smoke and not slow" -v
    pytest example_1_marked_tests.py -m "regression or smoke" -v

Зверніть увагу у виводі на рядок "N deselected / M selected".

Запуск: pytest example_1_marked_tests.py -v
"""

import pytest


@pytest.mark.smoke
def test_login():
    """Ключовий сценарій — smoke."""
    assert 1 + 1 == 2


@pytest.mark.smoke
def test_signup():
    """Ще один критичний шлях — smoke."""
    assert "user".upper() == "USER"


@pytest.mark.regression
def test_password_reset():
    """Регресійний сценарій."""
    assert [1, 2, 3][::-1] == [3, 2, 1]


@pytest.mark.regression
def test_profile_edit():
    """Ще один регресійний сценарій."""
    assert {"a": 1}.get("a") == 1


@pytest.mark.slow
@pytest.mark.regression
def test_full_report_generation():
    """Довгий регресійний тест — має і regression, і slow."""
    total = sum(range(100))
    assert total == 4950


@pytest.mark.slow
def test_bulk_import():
    """Повільний тест без regression."""
    assert len(list(range(1000))) == 1000


def test_health_check():
    """Тест без маркерів — його не відбере жоден -m <marker>."""
    assert True
