"""
Приклад 2: Retry, polling та search паттерни.
Запуск: pytest example_2_patterns.py -v
"""


def test_retry_pattern():
    """Retry — успіх на 3-й спробі."""
    responses = [500, 500, 200, 200]  # імітація
    attempt = 0
    result = None
    while attempt < len(responses):
        if responses[attempt] == 200:
            result = 200
            break
        attempt += 1
    assert result == 200
    assert attempt == 2  # 3-я спроба (індекс 2)


def test_retry_all_failed():
    """Retry — всі спроби невдалі."""
    responses = [500, 502, 503]
    attempt = 0
    result = None
    while attempt < len(responses):
        if responses[attempt] == 200:
            result = 200
            break
        attempt += 1
    assert result is None


def test_search_first():
    """Пошук першого елемента що відповідає умові."""
    items = [1, 3, 5, 8, 10, 12]
    index = 0
    found = None
    while index < len(items):
        if items[index] % 2 == 0:
            found = items[index]
            break
        index += 1
    assert found == 8


def test_max_iterations_guard():
    """Захист від нескінченного циклу."""
    max_iter = 100
    iterations = 0
    while iterations < max_iter:
        iterations += 1
        if iterations == 42:
            break
    assert iterations == 42