"""Вправа 1: парсинг requirements. Запуск: pytest exercise_1_requirements.py -v"""


def package_name(line):
    """'pytest==7.4.0' -> 'pytest'."""
    # TODO: return line.split("==")[0].strip()
    pass


def is_pinned(line):
    """True, якщо версія зафіксована через ==."""
    # TODO: return "==" in line
    pass


def count_deps(lines):
    """Порахувати залежності, ігноруючи коментарі (#) та порожні рядки."""
    # TODO:
    #   return len([l for l in lines if l.strip() and not l.strip().startswith("#")])
    pass


def test_package_name():
    # TODO: assert package_name("pytest==7.4.0") == "pytest"
    pass


def test_is_pinned_true():
    # TODO: assert is_pinned("requests==2.31.0") is True
    pass


def test_is_pinned_false():
    # TODO: assert is_pinned("requests>=2.25.0") is False
    pass


def test_count_deps():
    # TODO: assert count_deps(["pytest==7.4.0", "# comment", "", "requests==2.31.0"]) == 2
    pass


def test_count_deps_empty():
    # TODO: assert count_deps(["# only comment", ""]) == 0
    pass
