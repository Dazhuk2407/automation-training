"""Приклад 1: правила структури. Запуск: pytest example_1_structure_rules.py -v

Працюємо зі структурою проєкту як з ДАНИМИ: шлях до файлу — це рядок,
а ми лише класифікуємо його. Жодних реальних тек не створюємо.
"""


def is_test_file(path):
    name = path.split("/")[-1]
    return name.startswith("test_") or name.endswith("_test.py")

def is_config_file(path):
    name = path.split("/")[-1]
    config_names = {"requirements.txt", ".gitignore", "pytest.ini", "conftest.py"}
    return name in config_names

def classify_file(path):
    if is_test_file(path):
        return "test"
    if is_config_file(path):
        return "config"
    if path.endswith(".py"):
        return "source"
    return "other"

def test_is_test_file():
    assert is_test_file("tests/test_login.py") is True
    assert is_test_file("tests/login_test.py") is True
    assert is_test_file("src/app.py") is False

def test_is_config_file():
    assert is_config_file("requirements.txt") is True
    assert is_config_file("tests/conftest.py") is True
    assert is_config_file("src/app.py") is False

def test_classify_test():
    assert classify_file("tests/test_login.py") == "test"

def test_classify_config():
    assert classify_file("requirements.txt") == "config"

def test_classify_source():
    assert classify_file("src/app.py") == "source"

def test_classify_other():
    assert classify_file("README.md") == "other"
