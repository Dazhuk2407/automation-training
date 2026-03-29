"""
Вправа 4: Тестування граничних значень (boundary values).
Запуск: pytest exercise_4_boundaries.py -v
"""


def classify_age(age):
    if age < 13:
        return "child"
    elif age < 18:
        return "teen"
    elif age < 65:
        return "adult"
    else:
        return "senior"


def test_boundary_child_teen():
    """12 → child, 13 → teen."""
    # TODO: замініть pass на:
    #   assert classify_age(12) == "child"
    #   assert classify_age(13) == "teen"
    pass

def test_boundary_teen_adult():
    """17 → teen, 18 → adult."""
    # TODO: замініть pass на:
    #   assert classify_age(17) == "teen"
    #   assert classify_age(18) == "adult"
    pass

def test_boundary_adult_senior():
    """64 → adult, 65 → senior."""
    # TODO: замініть pass на:
    #   assert classify_age(64) == "adult"
    #   assert classify_age(65) == "senior"
    pass