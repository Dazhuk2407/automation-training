"""
Lesson 7: Example 2 - CLI Commands
Демонстрація команд для запуску з CLI
"""


def test_verbose():
    """Тест для -v (verbose)."""
    assert True


def test_quiet():
    """Тест для -q (quiet)."""
    assert 2 + 2 == 4


def test_with_print():
    """Тест для -s (show output)."""
    print("This is a print statement")
    print("Use pytest -s to see this")
    assert True


def test_pass():
    """Просто passing тест."""
    x = 10
    y = 10
    assert x == y


def test_fail_example():
    """❌ Цей тест падає (для демонстрації)."""
    # assert 5 > 10  # Закоментовано щоб не падав
    assert True


# Команди для запуску:
# pytest test_commands.py                    - базовий запуск
# pytest test_commands.py -v                 - verbose
# pytest test_commands.py -q                 - quiet
# pytest test_commands.py -s                 - show prints
# pytest test_commands.py -k "print"         - за ключовим словом
# pytest test_commands.py::test_pass -v      - один тест
# pytest test_commands.py -x                 - stop on first fail
# pytest test_commands.py --tb=short         - коротке трасування

