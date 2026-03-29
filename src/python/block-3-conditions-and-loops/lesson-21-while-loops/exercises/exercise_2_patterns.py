"""
Вправа 2: While паттерни — retry, search, queue.
Запуск: pytest exercise_2_patterns.py -v
"""


def test_retry_success():
    """Retry — знайти 200 у списку відповідей."""
    responses = [500, 502, 200, 200]
    # TODO: замініть pass на:
    #   attempt = 0
    #   result = None
    #   while attempt < len(responses):
    #       if responses[attempt] == 200:
    #           result = 200
    #           break
    #       attempt += 1
    #   assert result == 200
    pass


def test_retry_fail():
    """Retry — всі спроби невдалі."""
    responses = [500, 502, 503]
    # TODO: замініть pass на:
    #   attempt = 0
    #   result = None
    #   while attempt < len(responses):
    #       if responses[attempt] == 200:
    #           result = 200
    #           break
    #       attempt += 1
    #   assert result is None
    pass


def test_search_first_even():
    """Знайти перше парне число."""
    numbers = [1, 3, 5, 8, 10]
    # TODO: замініть pass на:
    #   i = 0
    #   found = None
    #   while i < len(numbers):
    #       if numbers[i] % 2 == 0:
    #           found = numbers[i]
    #           break
    #       i += 1
    #   assert found == 8
    pass


def test_consume_queue():
    """Обробити чергу до порожньої."""
    queue = ["a", "b", "c"]
    # TODO: замініть pass на:
    #   processed = []
    #   while queue:
    #       processed.append(queue.pop(0))
    #   assert processed == ["a", "b", "c"]
    #   assert queue == []
    pass