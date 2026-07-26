"""Приклад 3: організація файлів. Запуск: pytest example_3_organize.py -v

Беремо плаский список шляхів і розкладаємо його по категоріях
(dict: категорія -> список файлів). Це модель того, як структурується проєкт.
"""


def categorize(path):
    name = path.split("/")[-1]
    if name.startswith("test_") or name.endswith("_test.py"):
        return "tests"
    if name in {"requirements.txt", ".gitignore", "pytest.ini", "conftest.py"}:
        return "config"
    if path.endswith(".py"):
        return "source"
    return "docs"

def organize(paths):
    result = {"source": [], "tests": [], "config": [], "docs": []}
    for path in paths:
        result[categorize(path)].append(path)
    return result

def test_organize_groups():
    paths = [
        "src/app.py",
        "tests/test_app.py",
        "requirements.txt",
        "README.md",
    ]
    result = organize(paths)
    assert result["source"] == ["src/app.py"]
    assert result["tests"] == ["tests/test_app.py"]
    assert result["config"] == ["requirements.txt"]
    assert result["docs"] == ["README.md"]

def test_organize_empty():
    assert organize([]) == {"source": [], "tests": [], "config": [], "docs": []}

def test_categorize_test():
    assert categorize("tests/test_login.py") == "tests"
