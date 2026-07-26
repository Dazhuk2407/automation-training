"""Вправа 2: знайди й виправ баг. Запуск: pytest exercise_2_fix_requirements.py -v

Функції реалізовані, але в ОДНІЙ є `# BUG:`. Рівно один тест падає.
Знайди баг, виправ його — і всі 4 тести стануть зеленими.
"""


def parse_name(line):
    """'pytest==7.4.0' -> 'pytest'."""
    return line.split("==")[0].strip()


def parse_version(line):
    """'pytest==7.4.0' -> '7.4.0'."""
    # BUG: split на одинарному "=" замість "==" ламає розбір версії
    return line.split("=")[1].strip()


def is_pinned(line):
    """True, якщо версія зафіксована через ==."""
    return "==" in line


def count_deps(lines):
    """Кількість залежностей без коментарів (#) та порожніх рядків."""
    return len([l for l in lines if l.strip() and not l.strip().startswith("#")])


def test_parse_name():
    assert parse_name("pytest==7.4.0") == "pytest"


def test_parse_version():
    assert parse_version("pytest==7.4.0") == "7.4.0"


def test_is_pinned():
    assert is_pinned("requests==2.31.0") is True
    assert is_pinned("requests>=2.25.0") is False


def test_count_deps():
    assert count_deps(["pytest==7.4.0", "# comment", "", "requests==2.31.0"]) == 2
