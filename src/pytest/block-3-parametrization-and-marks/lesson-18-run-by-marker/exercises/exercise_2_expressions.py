"""
Вправа 2: Логічні вирази маркерів (and / or / not).

Функція `select_by_marker` уже готова (див. marker_selection.py).
Ваше завдання — замінити pass на правильний assert у кожному тесті.

Запуск: pytest exercise_2_expressions.py -v
"""

from marker_selection import select_by_marker


TESTS = [
    {"name": "test_login", "markers": {"smoke"}},
    {"name": "test_quick_check", "markers": {"smoke", "slow"}},
    {"name": "test_edge_case", "markers": {"regression"}},
    {"name": "test_report", "markers": {"regression", "slow"}},
    {"name": "test_health", "markers": set()},
]


def _names(tests):
    return [t["name"] for t in tests]


def test_smoke_and_not_slow():
    """`smoke and not slow` відбирає лише test_login."""
    selected = select_by_marker(TESTS, "smoke and not slow")
    # TODO: замініть pass на: assert _names(selected) == ["test_login"]
    pass


def test_smoke_or_regression():
    """`smoke or regression` відбирає всі, крім test_health."""
    selected = select_by_marker(TESTS, "smoke or regression")
    # TODO: замініть pass на:
    # assert _names(selected) == ["test_login", "test_quick_check", "test_edge_case", "test_report"]
    pass


def test_regression_and_not_slow():
    """`regression and not slow` відбирає лише test_edge_case."""
    selected = select_by_marker(TESTS, "regression and not slow")
    # TODO: замініть pass на: assert _names(selected) == ["test_edge_case"]
    pass


def test_not_slow():
    """`not slow` лишає test_health і відкидає slow-тести."""
    selected = select_by_marker(TESTS, "not slow")
    # TODO: замініть pass на: assert _names(selected) == ["test_login", "test_edge_case", "test_health"]
    pass


def test_smoke_and_slow():
    """`smoke and slow` відбирає лише test_quick_check."""
    selected = select_by_marker(TESTS, "smoke and slow")
    # TODO: замініть pass на: assert _names(selected) == ["test_quick_check"]
    pass
