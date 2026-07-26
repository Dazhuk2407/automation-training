"""
Приклад 3: Імперативний pytest.skip() всередині тесту.

Використовується коли рішення про пропуск залежить від даних,
доступних лише під час виконання (динамічна умова).
Після виклику pytest.skip(...) решта тесту не виконується.

Запуск: pytest example_3_imperative_skip.py -v
        pytest example_3_imperative_skip.py -rs
"""

import pytest


def load_config(available):
    """Імітація завантаження конфігу — може повернути None."""
    if not available:
        return None
    return {"enabled": True}


def test_config_available():
    """Конфіг доступний — тест виконується повністю."""
    config = load_config(available=True)
    if config is None:
        pytest.skip("конфіг недоступний")
    assert config["enabled"] is True


def test_config_missing():
    """Конфіг недоступний — тест пропускається зсередини."""
    config = load_config(available=False)
    if config is None:
        pytest.skip("конфіг недоступний у цьому середовищі")
    assert config["enabled"] is True  # не виконається — пропущено


def test_dataset_not_empty():
    """Динамічний пропуск: немає даних — пропускаємо."""
    data = []
    if not data:
        pytest.skip("порожній набір даних — нічого перевіряти")
    assert len(data) > 0  # не виконається — пропущено


def test_simple_pass():
    """Звичайний тест — виконується і проходить."""
    assert sum([1, 2, 3]) == 6


def test_feature_flag_on():
    """Прапорець увімкнено — тест виконується повністю."""
    feature_enabled = True
    if not feature_enabled:
        pytest.skip("фіча вимкнена прапорцем")
    assert feature_enabled is True
