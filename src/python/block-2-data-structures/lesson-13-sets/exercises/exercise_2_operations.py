"""
Вправа 2: Операції з множинами.
Запуск: pytest exercise_2_operations.py -v
"""


SMOKE = {"login", "search", "checkout"}
REGRESSION = {"login", "search", "checkout", "profile", "settings"}
API = {"login", "api_health", "api_users"}
UNIT = {"test_add", "test_subtract"}
E2E = {"test_checkout_flow", "test_login_flow"}


def test_union():
    """Об'єднання smoke та api."""
    # TODO: замініть pass на:
    #   all_tests = SMOKE | API
    #   assert "checkout" in all_tests
    #   assert "api_health" in all_tests
    pass


def test_intersection():
    """Спільні тести між smoke та api."""
    # TODO: замініть pass на:
    #   common = SMOKE & API
    #   assert common == {"login"}
    pass


def test_difference():
    """Тести тільки в regression, яких немає в smoke."""
    # TODO: замініть pass на:
    #   only_regression = REGRESSION - SMOKE
    #   assert only_regression == {"profile", "settings"}
    pass


def test_subset():
    """smoke — підмножина regression."""
    # TODO: замініть pass на: assert SMOKE <= REGRESSION
    pass


def test_disjoint():
    """unit та e2e не мають спільних тестів."""
    # TODO: замініть pass на: assert UNIT.isdisjoint(E2E)
    pass