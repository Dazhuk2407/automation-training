"""
Приклад 2: Логіка відбору за маркером — ЧИСТА функція.

Ми НЕ запускаємо тут справжній `pytest -m ...` (це показано лише у README).
Замість цього ми моделюємо відбір чистою функцією `select_by_marker`, щоб
її можна було протестувати звичайними assert.

Модель тесту — це dict:
    {"name": "test_login", "markers": {"smoke"}}

`select_by_marker(tests, expression)` повертає ті тести, чиї маркери
задовольняють вираз. У цьому файлі — прості випадки: одиночний маркер і `not`.

Запуск: pytest example_2_selection_logic.py -v
"""


def _match(markers, expression):
    """Обчислити булевий вираз маркерів для конкретного набору markers.

    Підтримка: одиночний маркер, not, and, or (без дужок — зліва направо
    за пріоритетом not > and > or).
    """
    tokens = expression.split()
    value, pos = _parse_or(tokens, 0, markers)
    if pos != len(tokens):
        raise ValueError(f"Неможливо розібрати вираз: {expression!r}")
    return value


def _parse_or(tokens, pos, markers):
    left, pos = _parse_and(tokens, pos, markers)
    while pos < len(tokens) and tokens[pos] == "or":
        right, pos = _parse_and(tokens, pos + 1, markers)
        left = left or right
    return left, pos


def _parse_and(tokens, pos, markers):
    left, pos = _parse_not(tokens, pos, markers)
    while pos < len(tokens) and tokens[pos] == "and":
        right, pos = _parse_not(tokens, pos + 1, markers)
        left = left and right
    return left, pos


def _parse_not(tokens, pos, markers):
    if pos < len(tokens) and tokens[pos] == "not":
        value, pos = _parse_not(tokens, pos + 1, markers)
        return (not value), pos
    marker = tokens[pos]
    return (marker in markers), pos + 1


def select_by_marker(tests, expression):
    """Повернути тести, чиї маркери задовольняють вираз (аналог pytest -m)."""
    return [t for t in tests if _match(t["markers"], expression)]


# ------------------------------------------------------------------
# Демонстраційний набір тестів (як «зібрана» база)
# ------------------------------------------------------------------

SAMPLE_TESTS = [
    {"name": "test_login", "markers": {"smoke"}},
    {"name": "test_signup", "markers": {"smoke"}},
    {"name": "test_edge_case", "markers": {"regression"}},
    {"name": "test_report", "markers": {"regression", "slow"}},
    {"name": "test_health", "markers": set()},
]


def _names(tests):
    return [t["name"] for t in tests]


# ------------------------------------------------------------------
# Тести чистої функції відбору
# ------------------------------------------------------------------

def test_select_single_marker():
    """`smoke` відбирає лише тести з маркером smoke."""
    selected = select_by_marker(SAMPLE_TESTS, "smoke")
    assert _names(selected) == ["test_login", "test_signup"]


def test_select_regression():
    """`regression` відбирає обидва regression-тести (у т.ч. той, що ще й slow)."""
    selected = select_by_marker(SAMPLE_TESTS, "regression")
    assert _names(selected) == ["test_edge_case", "test_report"]


def test_select_not_slow():
    """`not slow` відкидає лише slow, решту (навіть без маркерів) лишає."""
    selected = select_by_marker(SAMPLE_TESTS, "not slow")
    assert _names(selected) == [
        "test_login",
        "test_signup",
        "test_edge_case",
        "test_health",
    ]


def test_select_marker_without_matches():
    """Маркер, якого немає в наборі, дає порожній відбір."""
    selected = select_by_marker(SAMPLE_TESTS, "unit")
    assert selected == []


def test_untagged_test_not_selected_by_marker():
    """Тест без маркерів не потрапляє у відбір за конкретним маркером."""
    selected = select_by_marker(SAMPLE_TESTS, "smoke")
    assert "test_health" not in _names(selected)
