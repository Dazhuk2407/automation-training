"""
Приклад 2: Операції з множинами — union, intersection, difference.

Запуск: pytest example_2_operations.py -v
"""


SMOKE = {"login", "search", "checkout"}
REGRESSION = {"login", "search", "checkout", "profile", "settings"}
API_TESTS = {"login", "api_health", "api_users"}


def test_union():
    """Union — об'єднання всіх елементів."""
    all_tests = SMOKE | API_TESTS
    assert "login" in all_tests
    assert "api_health" in all_tests
    assert "checkout" in all_tests


def test_intersection():
    """Intersection — тільки спільні елементи."""
    common = SMOKE & API_TESTS
    assert common == {"login"}


def test_difference():
    """Difference — є в першому, немає в другому."""
    regression_only = REGRESSION - SMOKE
    assert regression_only == {"profile", "settings"}


def test_symmetric_difference():
    """Symmetric difference — є в одному АБО другому, але не в обох."""
    only_in_one = SMOKE ^ API_TESTS
    assert "login" not in only_in_one  # є в обох — не потрапляє
    assert "checkout" in only_in_one
    assert "api_health" in only_in_one


def test_subset():
    """Перевірка підмножини."""
    assert SMOKE <= REGRESSION  # smoke — підмножина regression
    assert SMOKE.issubset(REGRESSION)


def test_superset():
    """Перевірка надмножини."""
    assert REGRESSION >= SMOKE
    assert REGRESSION.issuperset(SMOKE)


def test_disjoint():
    """Перевірка що немає спільних елементів."""
    unit = {"test_add", "test_subtract"}
    e2e = {"test_checkout_flow", "test_login_flow"}
    assert unit.isdisjoint(e2e)