"""
Приклад 3: while у тестових сценаріях.
Запуск: pytest example_3_in_tests.py -v
"""


def consume_queue(queue):
    """Обробити чергу до порожньої."""
    processed = []
    while queue:
        item = queue.pop(0)
        processed.append(item)
    return processed


def find_threshold(values, threshold):
    """Знайти перше значення >= threshold."""
    i = 0
    while i < len(values):
        if values[i] >= threshold:
            return values[i]
        i += 1
    return None


def test_consume_queue():
    queue = ["task_1", "task_2", "task_3"]
    result = consume_queue(queue)
    assert result == ["task_1", "task_2", "task_3"]
    assert queue == []


def test_find_threshold_found():
    times = [50, 80, 120, 200, 350]
    assert find_threshold(times, 100) == 120


def test_find_threshold_not_found():
    times = [10, 20, 30]
    assert find_threshold(times, 100) is None


def test_retry_with_counter():
    """Симуляція retry з лічильником спроб."""
    max_retries = 3
    success_on = 2  # успіх на 2-й спробі
    attempt = 0
    success = False
    while attempt < max_retries:
        attempt += 1
        if attempt == success_on:
            success = True
            break
    assert success is True
    assert attempt == 2