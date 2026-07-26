"""
Приклад 3: Класифікація тестів у набори як ЧИСТА функція.

Замість запуску pytest ми моделюємо логіку "до якого набору належить тест"
звичайними функціями над множинами маркерів. Це легко тестувати і показує
принцип smoke ⊂ regression та поняття "uncategorized".

Запуск: pytest example_3_organize.py -v
"""


def suite_of(markers):
    """Повертає назву набору для тесту за його маркерами.

    Правила:
      {"smoke"}                 -> "smoke"
      {"regression"}            -> "regression"
      {"smoke", "regression"}   -> "smoke"  (smoke має пріоритет як швидший)
      без smoke/regression      -> "uncategorized"
    """
    if "smoke" in markers:
        return "smoke"
    if "regression" in markers:
        return "regression"
    return "uncategorized"


def count_suites(tests):
    """Підраховує, скільки тестів у кожному наборі.

    tests — це список множин маркерів (по одній на тест).
    Повертає словник {"smoke": n, "regression": n, "uncategorized": n}.
    """
    counts = {"smoke": 0, "regression": 0, "uncategorized": 0}
    for markers in tests:
        counts[suite_of(markers)] += 1
    return counts


# ============================================================
# Тести чистої функції suite_of
# ============================================================

def test_suite_of_smoke():
    assert suite_of({"smoke"}) == "smoke"


def test_suite_of_regression():
    assert suite_of({"regression"}) == "regression"


def test_suite_of_both_prefers_smoke():
    """smoke ⊂ regression: тест з обома маркерами рахуємо як smoke."""
    assert suite_of({"smoke", "regression"}) == "smoke"


def test_suite_of_uncategorized():
    assert suite_of(set()) == "uncategorized"
    assert suite_of({"slow"}) == "uncategorized"


# ============================================================
# Тести підрахунку наборів
# ============================================================

def test_count_suites():
    tests = [
        {"smoke", "regression"},   # -> smoke
        {"smoke"},                 # -> smoke
        {"regression"},            # -> regression
        {"regression", "slow"},    # -> regression
        {"slow"},                  # -> uncategorized
    ]
    counts = count_suites(tests)
    assert counts == {"smoke": 2, "regression": 2, "uncategorized": 1}


def test_count_suites_empty():
    assert count_suites([]) == {"smoke": 0, "regression": 0, "uncategorized": 0}
