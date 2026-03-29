"""
Вправа 1: Ітерація по колекціях.
Запуск: pytest exercise_1_basics.py -v
"""


def test_sum_list():
    """Порахувати суму [10, 20, 30] через for."""
    numbers = [10, 20, 30]
    # TODO: замініть pass на:
    #   total = 0
    #   for n in numbers:
    #       total += n
    #   assert total == 60
    pass


def test_count_chars():
    """Порахувати кількість символів 'l' у 'hello'."""
    text = "hello"
    # TODO: замініть pass на:
    #   count = 0
    #   for char in text:
    #       if char == "l":
    #           count += 1
    #   assert count == 2
    pass


def test_collect_keys():
    """Зібрати ключі словника в список."""
    config = {"host": "localhost", "port": 8080, "debug": True}
    # TODO: замініть pass на:
    #   keys = []
    #   for key in config:
    #       keys.append(key)
    #   assert "host" in keys
    #   assert len(keys) == 3
    pass


def test_range_squares():
    """Квадрати чисел 1-5."""
    # TODO: замініть pass на:
    #   squares = []
    #   for i in range(1, 6):
    #       squares.append(i ** 2)
    #   assert squares == [1, 4, 9, 16, 25]
    pass