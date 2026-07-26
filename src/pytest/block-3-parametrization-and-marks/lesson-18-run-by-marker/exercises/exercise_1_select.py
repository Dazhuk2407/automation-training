"""
Вправа 1: Відбір за одиночним маркером.

Функція `select_by_marker` уже готова (див. marker_selection.py).
Ваше завдання — замінити pass на правильний assert у кожному тесті.

Модель тесту: {"name": "test_x", "markers": {"smoke"}}

Запуск: pytest exercise_1_select.py -v
"""

from marker_selection import select_by_marker


TESTS = [
    {"name": "test_login", "markers": {"smoke"}},
    {"name": "test_signup", "markers": {"smoke"}},
    {"name": "test_edge_case", "markers": {"regression"}},
    {"name": "test_report", "markers": {"regression", "slow"}},
    {"name": "test_health", "markers": set()},
]


def _names(tests):
    return [t["name"] for t in tests]


def test_select_smoke():
    """`smoke` відбирає test_login та test_signup."""
    selected = select_by_marker(TESTS, "smoke")
    # TODO: замініть pass на: assert _names(selected) == ["test_login", "test_signup"]
    pass


def test_select_regression():
    """`regression` відбирає test_edge_case та test_report."""
    selected = select_by_marker(TESTS, "regression")
    # TODO: замініть pass на: assert _names(selected) == ["test_edge_case", "test_report"]
    pass


def test_select_slow():
    """`slow` відбирає лише test_report."""
    selected = select_by_marker(TESTS, "slow")
    # TODO: замініть pass на: assert _names(selected) == ["test_report"]
    pass


def test_select_unknown_marker_empty():
    """Маркера `unit` немає в наборі -> порожній відбір."""
    selected = select_by_marker(TESTS, "unit")
    # TODO: замініть pass на: assert selected == []
    pass


def test_untagged_not_selected():
    """test_health без маркерів не потрапляє у відбір за smoke."""
    selected = select_by_marker(TESTS, "smoke")
    # TODO: замініть pass на: assert "test_health" not in _names(selected)
    pass
