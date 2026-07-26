"""
Приклад 3: Симуляція кешу .pytest_cache між прогонами.

Реальний pytest пише список впалих у .pytest_cache і читає його при --lf.
Тут «кеш» — це простий dict у пам'яті: записуємо результати прогону,
потім читаємо їх для наступного --lf. Жодних файлів.

Запуск: pytest example_3_cache_state.py -v
"""


def write_cache(cache, results):
    """Записати результати прогону в кеш (перезаписує попередній стан).

    Зберігаємо лише впалі тести — саме так робить .pytest_cache/lastfailed.
    """
    cache["lastfailed"] = [
        name for name, status in results.items() if status == "failed"
    ]
    return cache


def read_last_failed(cache):
    """Прочитати список впалих із кешу (порожній, якщо кеша ще немає)."""
    return list(cache.get("lastfailed", []))


def test_write_then_read():
    """Після запису результатів кеш віддає лише впалі."""
    cache = {}
    write_cache(cache, {"test_a": "passed", "test_b": "failed"})
    assert read_last_failed(cache) == ["test_b"]


def test_empty_cache_reads_nothing():
    """Свіжий кеш (перший прогін) порожній."""
    cache = {}
    assert read_last_failed(cache) == []


def test_cache_is_overwritten_each_run():
    """Кеш перезаписується щопрогону, а не накопичується."""
    cache = {}
    write_cache(cache, {"test_a": "failed", "test_b": "passed"})
    assert read_last_failed(cache) == ["test_a"]

    # Наступний прогін: test_a виправлено, test_b впав
    write_cache(cache, {"test_a": "passed", "test_b": "failed"})
    assert read_last_failed(cache) == ["test_b"]


def test_all_green_clears_failed():
    """Коли все зелене — у кеші впалих не лишається."""
    cache = {}
    write_cache(cache, {"test_a": "failed"})
    write_cache(cache, {"test_a": "passed"})
    assert read_last_failed(cache) == []


def test_deleting_cache_loses_history():
    """Видалення кеша = втрата історії впалих (--lf знову ганяв би всі)."""
    cache = {}
    write_cache(cache, {"test_a": "failed"})
    cache.clear()  # аналог: rm -rf .pytest_cache
    assert read_last_failed(cache) == []
