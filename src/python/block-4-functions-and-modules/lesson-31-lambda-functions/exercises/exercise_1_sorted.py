"""Вправа 1: Lambda з sorted, min, max. Запуск: pytest exercise_1_sorted.py -v"""

USERS = [
    {"name": "Charlie", "score": 85},
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 70},
]

def test_sort_by_name():
    # TODO: замініть pass на:
    #   result = sorted(USERS, key=lambda u: u["name"])
    #   assert result[0]["name"] == "Alice"
    pass

def test_sort_by_score_desc():
    # TODO: замініть pass на:
    #   result = sorted(USERS, key=lambda u: u["score"], reverse=True)
    #   assert result[0]["name"] == "Alice"
    pass

def test_min_score():
    # TODO: замініть pass на:
    #   worst = min(USERS, key=lambda u: u["score"])
    #   assert worst["name"] == "Bob"
    pass

def test_max_score():
    # TODO: замініть pass на:
    #   best = max(USERS, key=lambda u: u["score"])
    #   assert best["name"] == "Alice"
    pass