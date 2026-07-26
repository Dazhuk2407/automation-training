"""Приклад 1: Парсинг requirements. Запуск: pytest example_1_parse_requirements.py -v

Парсимо текст requirements.txt ЯК РЯДКИ. Реальний pip не викликається.
"""

OPERATORS = ("==", ">=", "~=", "<=", "!=", ">", "<")


def parse_requirement(line):
    """'pytest==7.4.0' -> ('pytest', '==', '7.4.0')."""
    line = line.strip()
    for op in OPERATORS:
        if op in line:
            name, version = line.split(op, 1)
            return (name.strip(), op, version.strip())
    return (line, None, None)


def parse_requirements_text(text):
    """Розпарсити весь текст, ігноруючи коментарі (#) та порожні рядки."""
    result = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        result.append(parse_requirement(stripped))
    return result


def test_parse_pinned():
    assert parse_requirement("pytest==7.4.0") == ("pytest", "==", "7.4.0")


def test_parse_minimum():
    assert parse_requirement("requests>=2.25.0") == ("requests", ">=", "2.25.0")


def test_parse_no_version():
    assert parse_requirement("black") == ("black", None, None)


def test_parse_text_ignores_comments_and_blanks():
    text = """
# runtime
pytest==7.4.0

requests>=2.25.0
# кінець
"""
    assert parse_requirements_text(text) == [
        ("pytest", "==", "7.4.0"),
        ("requests", ">=", "2.25.0"),
    ]


def test_parse_text_empty():
    assert parse_requirements_text("# лише коментар\n\n") == []
