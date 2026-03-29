"""
Приклад 1: Базові CLI-команди.

Запускайте цей файл різними способами і порівнюйте вивід:
    pytest example_1_cli_basics.py -v     (детально)
    pytest example_1_cli_basics.py -q     (тихо)
    pytest example_1_cli_basics.py -s     (з print)
    pytest example_1_cli_basics.py --tb=short
"""


def test_addition():
    """Простий тест — пройде."""
    assert 2 + 3 == 5


def test_string():
    """Рядковий тест — пройде."""
    assert "hello".upper() == "HELLO"


def test_with_print():
    """Тест з print() — видно тільки з -s."""
    print("Цей текст видно тільки з pytest -s")
    assert True


def test_list():
    """Тест списку — пройде."""
    assert sorted([3, 1, 2]) == [1, 2, 3]


def test_failing_demo():
    """Тест для демонстрації падіння (закоментовано)."""
    # Розкоментуйте наступний рядок щоб побачити як pytest показує помилку:
    # assert 5 == 10
    assert True