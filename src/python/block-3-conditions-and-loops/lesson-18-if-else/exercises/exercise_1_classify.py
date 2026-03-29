"""
Вправа 1: Функції класифікації.
Запуск: pytest exercise_1_classify.py -v
"""


def classify_age(age):
    """Класифікувати вік: child / teen / adult / senior."""
    # TODO: замініть pass на:
    #   if age < 13:
    #       return "child"
    #   elif age < 18:
    #       return "teen"
    #   elif age < 65:
    #       return "adult"
    #   else:
    #       return "senior"
    pass


def classify_score(score):
    """Класифікувати оцінку: A / B / C / F."""
    # TODO: замініть pass на:
    #   if score >= 90:
    #       return "A"
    #   elif score >= 80:
    #       return "B"
    #   elif score >= 70:
    #       return "C"
    #   else:
    #       return "F"
    pass


def test_age_child():
    # TODO: замініть pass на: assert classify_age(5) == "child"
    pass

def test_age_teen():
    # TODO: замініть pass на: assert classify_age(15) == "teen"
    pass

def test_age_adult():
    # TODO: замініть pass на: assert classify_age(30) == "adult"
    pass

def test_age_senior():
    # TODO: замініть pass на: assert classify_age(70) == "senior"
    pass

def test_score_a():
    # TODO: замініть pass на: assert classify_score(95) == "A"
    pass

def test_score_f():
    # TODO: замініть pass на: assert classify_score(50) == "F"
    pass