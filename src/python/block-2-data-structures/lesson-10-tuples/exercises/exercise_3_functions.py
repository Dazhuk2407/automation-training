"""
Вправа 3: Функції, що повертають tuples.
Запуск: pytest exercise_3_functions.py -v
"""


def min_max(numbers):
    """Повертає tuple (мінімум, максимум) зі списку чисел."""
    # TODO: замініть pass на: return min(numbers), max(numbers)
    pass


def split_name(full_name):
    """Розділяє 'Alice Smith' на ('Alice', 'Smith')."""
    # TODO: замініть pass на:
    #   parts = full_name.split()
    #   return parts[0], parts[1]
    pass


def http_status(code):
    """Повертає (code, message) для HTTP коду."""
    # TODO: замініть pass на:
    #   messages = {200: "OK", 404: "Not Found", 500: "Server Error"}
    #   return code, messages.get(code, "Unknown")
    pass


# --- Тести ---

def test_min_max():
    """min_max повертає правильний tuple."""
    result = min_max([5, 2, 8, 1, 9])
    # TODO: замініть pass на:
    #   assert result == (1, 9)
    pass


def test_min_max_unpacking():
    """min_max результат можна розпакувати."""
    minimum, maximum = min_max([10, 20, 30])
    # TODO: замініть pass на:
    #   assert minimum == 10
    #   assert maximum == 30
    pass


def test_split_name():
    """split_name розділяє ім'я правильно."""
    first, last = split_name("Alice Smith")
    # TODO: замініть pass на:
    #   assert first == "Alice"
    #   assert last == "Smith"
    pass


def test_http_status():
    """http_status повертає правильний tuple."""
    code, message = http_status(404)
    # TODO: замініть pass на:
    #   assert code == 404
    #   assert message == "Not Found"
    pass