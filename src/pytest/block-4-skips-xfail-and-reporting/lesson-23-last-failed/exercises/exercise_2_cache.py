"""
Вправа 2: Кеш між прогонами (запис/читання).

Функції write_cache() і read_last_failed() вже надано — НЕ змінюйте їх.
Ваше завдання: замінити pass на правильний assert у кожному тесті.

Нагадування:
- у кеші зберігаються ЛИШЕ впалі тести;
- кеш перезаписується щопрогону (не накопичується);
- порожній/очищений кеш → впалих немає.

Запуск: pytest exercise_2_cache.py -v
"""


def write_cache(cache, results):
    """Записати впалі тести прогону в кеш (готова, не змінювати)."""
    cache["lastfailed"] = [
        name for name, status in results.items() if status == "failed"
    ]
    return cache


def read_last_failed(cache):
    """Прочитати впалі з кешу (готова, не змінювати)."""
    return list(cache.get("lastfailed", []))


def test_write_then_read():
    """Після запису кеш віддає лише впалий test_b."""
    cache = {}
    write_cache(cache, {"test_a": "passed", "test_b": "failed"})
    # TODO: замініть pass на: assert read_last_failed(cache) == ["test_b"]
    pass


def test_fresh_cache_empty():
    """Свіжий кеш порожній (впалих немає)."""
    cache = {}
    # TODO: замініть pass на: assert read_last_failed(cache) == []
    pass


def test_cache_overwritten():
    """Другий прогін перезаписує кеш новими впалими."""
    cache = {}
    write_cache(cache, {"test_a": "failed", "test_b": "passed"})
    write_cache(cache, {"test_a": "passed", "test_b": "failed"})
    # TODO: замініть pass на: assert read_last_failed(cache) == ["test_b"]
    pass


def test_all_green_clears_failed():
    """Прогін, де все зелене, лишає кеш без впалих."""
    cache = {}
    write_cache(cache, {"test_a": "failed"})
    write_cache(cache, {"test_a": "passed"})
    # TODO: замініть pass на: assert read_last_failed(cache) == []
    pass


def test_clearing_cache_loses_history():
    """Очищення кеша = втрата історії впалих."""
    cache = {}
    write_cache(cache, {"test_a": "failed"})
    cache.clear()
    # TODO: замініть pass на: assert read_last_failed(cache) == []
    pass
