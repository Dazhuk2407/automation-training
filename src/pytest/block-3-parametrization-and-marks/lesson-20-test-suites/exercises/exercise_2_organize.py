"""
Вправа 2: Підрахунок тестів у наборах.

Функція count_suites вже написана. Вона приймає список множин маркерів
(по одній на тест) і повертає словник з кількістю тестів у кожному наборі.
Замініть pass на правильний assert у кожному тесті.

Запуск: pytest exercise_2_organize.py -v
"""


def suite_of(markers):
    if "smoke" in markers:
        return "smoke"
    if "regression" in markers:
        return "regression"
    return "uncategorized"


def count_suites(tests):
    counts = {"smoke": 0, "regression": 0, "uncategorized": 0}
    for markers in tests:
        counts[suite_of(markers)] += 1
    return counts


def test_count_empty():
    """Порожній список — усі лічильники по нулю."""
    # TODO: замініть pass на:
    # assert count_suites([]) == {"smoke": 0, "regression": 0, "uncategorized": 0}
    pass


def test_count_only_smoke():
    """Два smoke-тести -> smoke=2."""
    tests = [{"smoke"}, {"smoke"}]
    # TODO: замініть pass на: assert count_suites(tests)["smoke"] == 2
    pass


def test_count_mixed():
    """Змішаний набір -> перевірте повний словник."""
    tests = [{"smoke", "regression"}, {"regression"}, {"slow"}]
    # TODO: замініть pass на:
    # assert count_suites(tests) == {"smoke": 1, "regression": 1, "uncategorized": 1}
    pass


def test_count_smoke_subset_of_regression():
    """Тест з обома маркерами рахується як smoke, не як regression."""
    tests = [{"smoke", "regression"}]
    # TODO: замініть pass на: assert count_suites(tests)["regression"] == 0
    pass


def test_count_uncategorized():
    """Тест без smoke/regression потрапляє в uncategorized."""
    tests = [{"slow"}, set()]
    # TODO: замініть pass на: assert count_suites(tests)["uncategorized"] == 2
    pass
