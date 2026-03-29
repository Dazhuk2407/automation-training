"""Вправа 1: return, None, early return. Запуск: pytest exercise_1_return.py -v"""


def absolute(n):
    # TODO: return n if n >= 0 else -n
    pass

def validate_age(age):
    """'invalid' якщо < 0 або > 150, інакше 'valid'."""
    # TODO:
    #   if age < 0 or age > 150:
    #       return "invalid"
    #   return "valid"
    pass

def first_negative(numbers):
    """Перше від'ємне число або None."""
    # TODO:
    #   for n in numbers:
    #       if n < 0:
    #           return n
    #   return None
    pass

def test_absolute():
    # TODO: assert absolute(-5) == 5 та assert absolute(3) == 3
    pass

def test_validate_age():
    # TODO: assert validate_age(25) == "valid" та assert validate_age(-1) == "invalid"
    pass

def test_first_negative_found():
    # TODO: assert first_negative([1, 2, -3, 4]) == -3
    pass

def test_first_negative_none():
    # TODO: assert first_negative([1, 2, 3]) is None
    pass