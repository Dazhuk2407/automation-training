"""
Приклад 4: print() у тестах — видно тільки з -s.

Запуск без -s:  pytest example_4_print_output.py -v      (print прихований)
Запуск з -s:    pytest example_4_print_output.py -v -s    (print видно)
"""


def test_with_prints():
    """Тест з print() — порівняйте вивід з -s та без."""
    print(">>> Крок 1: підготовка даних")
    data = [1, 2, 3]
    print(f">>> Крок 2: data = {data}")
    data.append(4)
    print(f">>> Крок 3: після append = {data}")
    assert len(data) == 4


def test_without_prints():
    """Тест без print() — для порівняння."""
    assert 2 + 2 == 4