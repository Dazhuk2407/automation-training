"""
Lesson 4: Example 3 - File Naming Patterns
Демонстрація різних патернів назв файлів
"""


def test_file_pattern_example():
    """
    Цей файл називається test_file_patterns.py

    Pytest знайде його, бо він починається з 'test_'

    Інші валідні назви:
    - test_calculator.py ✅
    - test_api.py ✅
    - test_user_auth.py ✅
    - calculator_test.py ✅ (закінчується на _test)
    - api_test.py ✅

    Невалідні назви:
    - calculator.py ❌
    - testcalculator.py ❌ (без підкреслення)
    - my_tests.py ❌ (не починається з test_)
    """
    assert True


def test_discovery_in_subdirectories():
    """
    Pytest шукає тести рекурсивно:

    tests/
    ├── test_unit/
    │   ├── test_models.py  ✅ буде знайдено
    │   └── test_utils.py   ✅ буде знайдено
    └── test_integration/
        └── test_api.py     ✅ буде знайдено
    """
    assert True


def test_conftest_special_file():
    """
    conftest.py - спеціальний файл:
    - Не потребує test_ префікса
    - Автоматично завантажується pytest
    - Містить fixtures та конфігурацію
    """
    assert True


# Запустіть з кореня проекту:
# pytest -v                    # знайде всі тести
# pytest tests/                # тести тільки в tests/
# pytest tests/test_unit/      # тести тільки в test_unit/

