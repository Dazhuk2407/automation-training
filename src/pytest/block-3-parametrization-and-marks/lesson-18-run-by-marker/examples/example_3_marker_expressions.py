"""
Приклад 3: Складені вирази маркерів — and / or / комбінації.

Той самий підхід, що й у прикладі 2: моделюємо `pytest -m "<вираз>"`
чистою функцією `select_by_marker` і перевіряємо результат через assert.

Тут ми фокусуємось на логічних виразах:
    "smoke and not slow"
    "smoke or regression"
    "regression and not slow"

Запуск: pytest example_3_marker_expressions.py -v
"""

from example_2_selection_logic import select_by_marker


SAMPLE_TESTS = [
    {"name": "test_login", "markers": {"smoke"}},
    {"name": "test_quick_check", "markers": {"smoke", "slow"}},
    {"name": "test_edge_case", "markers": {"regression"}},
    {"name": "test_report", "markers": {"regression", "slow"}},
    {"name": "test_health", "markers": set()},
]


def _names(tests):
    return [t["name"] for t in tests]


def test_smoke_and_not_slow():
    """`smoke and not slow` — smoke, але без slow."""
    selected = select_by_marker(SAMPLE_TESTS, "smoke and not slow")
    assert _names(selected) == ["test_login"]


def test_smoke_or_regression():
    """`smoke or regression` — об'єднаний набір smoke + regression."""
    selected = select_by_marker(SAMPLE_TESTS, "smoke or regression")
    assert _names(selected) == [
        "test_login",
        "test_quick_check",
        "test_edge_case",
        "test_report",
    ]


def test_regression_and_not_slow():
    """`regression and not slow` — регрес без повільних."""
    selected = select_by_marker(SAMPLE_TESTS, "regression and not slow")
    assert _names(selected) == ["test_edge_case"]


def test_smoke_and_slow():
    """`smoke and slow` — обидва маркери одночасно."""
    selected = select_by_marker(SAMPLE_TESTS, "smoke and slow")
    assert _names(selected) == ["test_quick_check"]


def test_not_slow_keeps_untagged():
    """`not slow` лишає й тест без маркерів."""
    selected = select_by_marker(SAMPLE_TESTS, "not slow")
    assert "test_health" in _names(selected)
    assert "test_report" not in _names(selected)
