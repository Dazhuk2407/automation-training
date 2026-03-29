"""
Вправа 2: Тестування рядкових функцій

Функції reverse_string та is_palindrome вже написані.
Ваше завдання — дописати тести.

Запуск: pytest exercise_2_string_utils.py -v
"""


# --- Готові функції (НЕ змінюйте!) ---

def reverse_string(s):
    """Повертає рядок у зворотному порядку."""
    return s[::-1]


def is_palindrome(s):
    """Повертає True якщо рядок — паліндром (без урахування регістру)."""
    s_lower = s.lower()
    return s_lower == s_lower[::-1]


# --- Ваші тести (допишіть замість pass) ---

def test_reverse_hello():
    """reverse_string("hello") має повернути "olleh"."""
    # TODO: замініть pass на: assert reverse_string("hello") == "olleh"
    pass


def test_reverse_empty():
    """reverse_string("") має повернути ""."""
    # TODO: замініть pass на: assert reverse_string("") == ""
    pass


def test_palindrome_racecar():
    """is_palindrome("racecar") має повернути True."""
    # TODO: замініть pass на: assert is_palindrome("racecar") is True
    pass


def test_palindrome_hello():
    """is_palindrome("hello") має повернути False."""
    # TODO: замініть pass на: assert is_palindrome("hello") is False
    pass


def test_palindrome_case_insensitive():
    """is_palindrome("Madam") має повернути True (регістр не важливий)."""
    # TODO: замініть pass на: assert is_palindrome("Madam") is True
    pass