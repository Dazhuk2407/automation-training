"""
Готова реалізація логіки відбору за маркером для вправ Lesson 18.

Ви НЕ редагуєте цей файл. Ви лише викликаєте `select_by_marker` у своїх
тестах і перевіряєте результат через assert.

Модель тесту — це dict: {"name": "test_login", "markers": {"smoke"}}.
Вираз підтримує: одиночний маркер, not, and, or (пріоритет: not > and > or).
"""


def _match(markers, expression):
    tokens = expression.split()
    value, pos = _parse_or(tokens, 0, markers)
    if pos != len(tokens):
        raise ValueError(f"Неможливо розібрати вираз: {expression!r}")
    return value


def _parse_or(tokens, pos, markers):
    left, pos = _parse_and(tokens, pos, markers)
    while pos < len(tokens) and tokens[pos] == "or":
        right, pos = _parse_and(tokens, pos + 1, markers)
        left = left or right
    return left, pos


def _parse_and(tokens, pos, markers):
    left, pos = _parse_not(tokens, pos, markers)
    while pos < len(tokens) and tokens[pos] == "and":
        right, pos = _parse_not(tokens, pos + 1, markers)
        left = left and right
    return left, pos


def _parse_not(tokens, pos, markers):
    if pos < len(tokens) and tokens[pos] == "not":
        value, pos = _parse_not(tokens, pos + 1, markers)
        return (not value), pos
    marker = tokens[pos]
    return (marker in markers), pos + 1


def select_by_marker(tests, expression):
    """Повернути тести, чиї маркери задовольняють вираз (аналог pytest -m)."""
    return [t for t in tests if _match(t["markers"], expression)]
