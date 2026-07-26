"""
Приклад 3: порівняння scope — function vs class vs module в одному файлі.

Три фікстури з різними scope і власними лічильниками. Три тести в одному
класі використовують усі три. Наприкінці — перевірка, скільки разів
виконався setup кожної:

    function → 3 рази (по разу на тест)
    class    → 1 раз  (один клас з 3 тестами)
    module   → 1 раз  (один файл)

Запуск: pytest example_3_scope_compare.py -v
"""

import pytest


fn_calls = {"n": 0}
cls_calls = {"n": 0}
mod_calls = {"n": 0}


@pytest.fixture  # function scope (default)
def fn_fixture():
    fn_calls["n"] += 1
    return fn_calls["n"]


@pytest.fixture(scope="class")
def cls_fixture():
    cls_calls["n"] += 1
    return cls_calls["n"]


@pytest.fixture(scope="module")
def mod_fixture():
    mod_calls["n"] += 1
    return mod_calls["n"]


class TestScopeCompare:
    """Три тести в одному класі використовують усі три фікстури."""

    def test_one(self, fn_fixture, cls_fixture, mod_fixture):
        assert fn_fixture == 1   # function: створена вперше
        assert cls_fixture == 1  # class: створена вперше
        assert mod_fixture == 1  # module: створена вперше

    def test_two(self, fn_fixture, cls_fixture, mod_fixture):
        assert fn_fixture == 2   # function: НОВА (setup вдруге)
        assert cls_fixture == 1  # class: та сама (setup не повторився)
        assert mod_fixture == 1  # module: та сама

    def test_three(self, fn_fixture, cls_fixture, mod_fixture):
        assert fn_fixture == 3   # function: знову нова
        assert cls_fixture == 1  # class: та сама
        assert mod_fixture == 1  # module: та сама


def test_setup_counts():
    """Підсумок: скільки разів виконався setup кожної фікстури."""
    assert fn_calls["n"] == 3   # function — по разу на кожен тест
    assert cls_calls["n"] == 1  # class — один раз на клас
    assert mod_calls["n"] == 1  # module — один раз на файл
