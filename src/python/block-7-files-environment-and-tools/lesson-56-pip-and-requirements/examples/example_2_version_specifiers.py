"""Приклад 2: Специфікатори версій. Запуск: pytest example_2_version_specifiers.py -v

Класифікуємо специфікатори з рядків requirements. Реальний pip не викликається.
"""


def classify_specifier(line):
    """'pytest==7.4.0' -> 'pinned'; '>=' -> 'minimum'; '~=' -> 'compatible'; '<' -> 'upper'."""
    line = line.strip()
    if "==" in line:
        return "pinned"
    if ">=" in line:
        return "minimum"
    if "~=" in line:
        return "compatible"
    if "<" in line:
        return "upper"
    return "unpinned"


def is_pinned(line):
    """True, якщо версія жорстко зафіксована через ==."""
    return "==" in line


def count_pinned(lines):
    """Скільки залежностей у списку запінено."""
    return sum(1 for line in lines if is_pinned(line))


def test_classify_pinned():
    assert classify_specifier("pytest==7.4.0") == "pinned"


def test_classify_minimum():
    assert classify_specifier("requests>=2.25.0") == "minimum"


def test_classify_compatible():
    assert classify_specifier("flask~=1.4") == "compatible"


def test_classify_upper():
    assert classify_specifier("numpy<2.0") == "upper"


def test_classify_unpinned():
    assert classify_specifier("black") == "unpinned"


def test_is_pinned():
    assert is_pinned("pytest==7.4.0") is True
    assert is_pinned("requests>=2.25.0") is False


def test_count_pinned():
    deps = ["pytest==7.4.0", "requests>=2.25.0", "flask==2.0.0"]
    assert count_pinned(deps) == 2
