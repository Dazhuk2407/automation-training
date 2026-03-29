"""Вправа 1: Функції з docstrings. Запуск: pytest exercise_1_docstrings.py -v"""


def is_valid_email(email):
    """Перевірити що email не порожній і містить '@'."""
    # TODO: return bool(email) and "@" in email
    pass

def format_name(first, last):
    """Форматувати повне ім'я: 'First Last'.

    Args:
        first: Ім'я.
        last: Прізвище.

    Returns:
        Рядок "First Last".
    """
    # TODO: return f"{first} {last}"
    pass

def calculate_average(numbers):
    """Розрахувати середнє значення списку чисел.

    Args:
        numbers: Список чисел.

    Returns:
        Середнє значення або 0 якщо список порожній.
    """
    # TODO:
    #   if not numbers:
    #       return 0
    #   return sum(numbers) / len(numbers)
    pass


def test_email():
    # TODO: assert is_valid_email("a@b.com") is True
    pass

def test_email_has_doc():
    # TODO: assert is_valid_email.__doc__ is not None
    pass

def test_format_name():
    # TODO: assert format_name("Alice", "Smith") == "Alice Smith"
    pass

def test_average():
    # TODO: assert calculate_average([10, 20, 30]) == 20.0
    pass

def test_average_empty():
    # TODO: assert calculate_average([]) == 0
    pass