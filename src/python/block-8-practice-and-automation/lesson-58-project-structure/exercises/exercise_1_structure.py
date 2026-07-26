"""Вправа 1: структура проєкту. Запуск: pytest exercise_1_structure.py -v"""


def is_test_file(path):
    # TODO: return True якщо ім'я файла починається з "test_" або закінчується на "_test.py"
    pass

def is_source_file(path):
    # TODO: return True якщо файл .py і НЕ тестовий (використай is_test_file)
    pass

def classify_file(path):
    # TODO: return "test" / "source" / "other" залежно від типу файла
    pass

def test_is_test_file_true():
    # TODO: assert is_test_file("tests/test_login.py") is True
    pass

def test_is_test_file_false():
    # TODO: assert is_test_file("src/app.py") is False
    pass

def test_is_source_file():
    # TODO: assert is_source_file("src/app.py") is True
    pass

def test_classify_test():
    # TODO: assert classify_file("tests/test_login.py") == "test"
    pass

def test_classify_other():
    # TODO: assert classify_file("README.md") == "other"
    pass
