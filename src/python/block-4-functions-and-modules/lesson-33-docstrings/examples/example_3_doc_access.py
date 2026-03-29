"""Приклад 3: Доступ до docstrings. Запуск: pytest example_3_doc_access.py -v"""


def add(a, b):
    """Додати два числа."""
    return a + b


def no_doc(x):
    return x


def test_doc_attribute():
    """Docstring доступний через __doc__."""
    assert add.__doc__ == "Додати два числа."


def test_no_doc():
    """Функція без docstring має __doc__ == None."""
    assert no_doc.__doc__ is None


def test_doc_in_test():
    """Цей docstring видно у pytest -v."""
    assert True