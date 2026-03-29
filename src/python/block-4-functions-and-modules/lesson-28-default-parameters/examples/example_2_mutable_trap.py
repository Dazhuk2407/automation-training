"""
Приклад 2: Mutable default argument — пастка та рішення.
Запуск: pytest example_2_mutable_trap.py -v
"""


def add_tag_bad(tag, tags=[]):
    """❌ Mutable default — tags спільний між викликами."""
    tags.append(tag)
    return tags


def add_tag_good(tag, tags=None):
    """✅ None як default — кожен виклик отримує свій список."""
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


def test_mutable_trap():
    """Демонстрація пастки: другий виклик бачить дані першого."""
    result1 = add_tag_bad("smoke")
    result2 = add_tag_bad("api")
    # result2 містить і "smoke", і "api"!
    assert result2 == ["smoke", "api"]


def test_fixed_version():
    """None як default — кожен виклик ізольований."""
    result1 = add_tag_good("smoke")
    result2 = add_tag_good("api")
    assert result1 == ["smoke"]
    assert result2 == ["api"]  # ✅ тільки "api"


def test_pass_existing_list():
    """Можна передати існуючий список."""
    existing = ["unit"]
    result = add_tag_good("integration", tags=existing)
    assert result == ["unit", "integration"]