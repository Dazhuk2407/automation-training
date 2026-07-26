"""Вправа 2: знайди та виправ баг. Запуск: pytest exercise_2_fix_structure.py -v

Один із тестів падає через `# BUG:` у коді. Знайди його, виправ функцію
і переконайся, що всі тести проходять.
"""


def is_test_file(path):
    name = path.split("/")[-1]
    # BUG: перевіряє тільки ".endswith('test.py')", тому пропускає файли "test_login.py"
    return name.endswith("test.py")

def is_config_file(path):
    name = path.split("/")[-1]
    return name in {"requirements.txt", ".gitignore", "pytest.ini", "conftest.py"}

def classify_file(path):
    if is_test_file(path):
        return "test"
    if is_config_file(path):
        return "config"
    if path.endswith(".py"):
        return "source"
    return "other"

def test_is_test_file_prefix():
    assert is_test_file("tests/test_login.py") is True

def test_is_test_file_source():
    assert is_test_file("src/app.py") is False

def test_is_config_file():
    assert is_config_file("requirements.txt") is True

def test_classify_config():
    assert classify_file("pytest.ini") == "config"
