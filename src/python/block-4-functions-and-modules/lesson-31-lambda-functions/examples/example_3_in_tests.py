"""Приклад 3: Lambda у тестових сценаріях. Запуск: pytest example_3_in_tests.py -v"""


def test_sort_responses_by_time():
    responses = [
        {"url": "/api", "time_ms": 150},
        {"url": "/auth", "time_ms": 30},
        {"url": "/data", "time_ms": 200},
    ]
    fastest = min(responses, key=lambda r: r["time_ms"])
    assert fastest["url"] == "/auth"


def test_sort_errors_first():
    results = [
        {"test": "login", "status": "passed"},
        {"test": "checkout", "status": "failed"},
        {"test": "search", "status": "passed"},
    ]
    # failed першими (False < True, тому інвертуємо)
    sorted_results = sorted(results, key=lambda r: r["status"] != "failed")
    assert sorted_results[0]["test"] == "checkout"


def test_filter_active_users():
    users = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
        {"name": "Charlie", "active": True},
    ]
    active = list(filter(lambda u: u["active"], users))
    assert len(active) == 2


def test_extract_names_with_map():
    users = [{"name": "Alice"}, {"name": "Bob"}]
    names = list(map(lambda u: u["name"], users))
    assert names == ["Alice", "Bob"]