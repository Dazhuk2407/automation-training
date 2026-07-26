"""Автоматична перевірка — Lesson 36"""
import ast, os, pytest
D = os.path.dirname(os.path.abspath(__file__))
F = ["exercise_1_identify.py", "exercise_2_fix_errors.py"]
E = {"exercise_1_identify.py": 5, "exercise_2_fix_errors.py": 4}
def _fp(f): return os.path.join(D, f)
def _t(fp):
    with open(fp, encoding="utf-8") as f: t = ast.parse(f.read())
    return [n.name for n in ast.walk(t) if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]
def _a(fp, fn):
    with open(fp, encoding="utf-8") as f: t = ast.parse(f.read())
    for n in ast.walk(t):
        if isinstance(n, ast.FunctionDef) and n.name == fn:
            for c in ast.walk(n):
                if isinstance(c, ast.Assert): return True
    return False
class TestFiles:
    @pytest.mark.parametrize("f", F)
    def test_exists(self, f): assert os.path.isfile(_fp(f))
class TestCounts:
    @pytest.mark.parametrize("f,e", E.items())
    def test_count(self, f, e):
        fp = _fp(f)
        if not os.path.isfile(fp): pytest.skip()
        assert len(_t(fp)) >= e
class TestAsserts:
    @pytest.mark.parametrize("f", F)
    def test_asserts(self, f):
        fp = _fp(f)
        if not os.path.isfile(fp): pytest.skip()
        m = [t for t in _t(fp) if not _a(fp, t)]
        assert not m, f"{f}: без assert: {', '.join(m)}"
class TestPass:
    @pytest.mark.parametrize("f", F)
    def test_pass(self, f):
        fp = _fp(f)
        if not os.path.isfile(fp): pytest.skip()
        assert pytest.main([fp, "-v", "--tb=short", "-q", "--no-header"]) == 0
