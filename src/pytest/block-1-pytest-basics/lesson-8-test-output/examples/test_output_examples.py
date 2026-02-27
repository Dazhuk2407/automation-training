"""
Lesson 8: Example 1 - Test Output Analysis
Демонстрація різних виводів та помилок
"""


def test_passing():
    """Цей тест проходить."""
    assert 2 + 2 == 4


def test_failing_assertion():
    """❌ Цей тест падає на assertion."""
    x = 5
    # assert x == 10  # Закоментовано для запуску інших тестів


def test_with_message():
    """Тест з повідомленням."""
    x = 10
    y = 5
    assert x > y, f"Expected {x} > {y}"


def test_print_output():
    """Тест з print() для запуску з -s."""
    print("This output shows with pytest -s")
    print("Use pytest -s to see print statements")
    assert True


def test_multiple_asserts():
    """Тест з кількома assertions."""
    assert 1 + 1 == 2
    assert "test" in "pytest"
    assert [1, 2, 3] != []
    assert True


def test_exception_handling():
    """Тест що работает с виключеннями."""
    try:
        result = 10 / 0
    except ZeroDivisionError:
        assert True  # Очекиваємо виключення


# Запустіть:
# pytest test_output.py -v          - verbose
# pytest test_output.py -s          - show prints
# pytest test_output.py --tb=short  - коротке трасування
# pytest test_output.py::test_failing_assertion -v  - один тест

