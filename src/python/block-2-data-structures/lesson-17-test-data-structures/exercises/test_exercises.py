"""
Автоматична перевірка — Lesson 17: Test Data Structures
Запуск: pytest test_exercises.py -v
"""
import ast, os, pytest

EXERCISES_DIR = os.path.dirname(os.path.abspath(__file__))
FILES = ["exercise_1_navigation.py", "exercise_2_validation.py", "exercise_3_factory.py", "exercise_4_real_api.py"]
EXPECTED = {"exercise_1_navigation.py": 4, "exercise_2_validation.py": 4, "exercise_3_factory.py": 3, "exercise_4_real_api.py": 4}

def _fp(f): return os.path.join(EXERCISES_DIR, f)
def _tests(fp):
    with open(fp, encoding="utf-8") as f: tree = ast.parse(f.read())
    return [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]
def _has_assert(fp, fn):
    with open(fp, encoding="utf-8") as f: tree = ast.parse(f.read())
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == fn:
            for c in ast.walk(n):
                if isinstance(c, ast.Assert): return True
    return False

class TestFiles:
    @pytest.mark.parametrize("f", FILES)
    def test_exists(self, f): assert os.path.isfile(_fp(f)), f"Створіть {f}"

class TestCounts:
    @pytest.mark.parametrize("f,exp", EXPECTED.items())
    def test_count(self, f, exp):
        fp = _fp(f)
        if not os.path.isfile(fp): pytest.skip()
        assert len(_tests(fp)) >= exp

class TestAsserts:
    @pytest.mark.parametrize("f", FILES)
    def test_asserts(self, f):
        fp = _fp(f)
        if not os.path.isfile(fp): pytest.skip()
        missing = [t for t in _tests(fp) if not _has_assert(fp, t)]
        assert not missing, f"{f}: без assert: {', '.join(missing)}"

class TestPass:
    @pytest.mark.parametrize("f", FILES)
    def test_pass(self, f):
        fp = _fp(f)
        if not os.path.isfile(fp): pytest.skip()
        assert pytest.main([fp, "-v", "--tb=short", "-q", "--no-header"]) == 0