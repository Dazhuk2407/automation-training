"""
Автоматична перевірка — Lesson 14: Mutable vs Immutable
Запуск: pytest test_exercises.py -v
"""

import ast
import os
import pytest

EXERCISES_DIR = os.path.dirname(os.path.abspath(__file__))
EXERCISE_FILES = ["exercise_1_identify.py", "exercise_2_side_effects.py", "exercise_3_safe_tests.py"]
EXPECTED = {"exercise_1_identify.py": 5, "exercise_2_side_effects.py": 3, "exercise_3_safe_tests.py": 4}


def _fp(f):
    return os.path.join(EXERCISES_DIR, f)


def _tests(fp):
    with open(fp, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    return [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]


def _has_assert(fp, fn):
    with open(fp, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == fn:
            for c in ast.walk(n):
                if isinstance(c, ast.Assert):
                    return True
                if isinstance(c, ast.With):
                    for item in c.items:
                        if isinstance(item.context_expr, ast.Call):
                            call = item.context_expr
                            if isinstance(call.func, ast.Attribute) and call.func.attr == "raises":
                                return True
    return False


class TestFilesExist:
    @pytest.mark.parametrize("f", EXERCISE_FILES)
    def test_exists(self, f):
        assert os.path.isfile(_fp(f)), f"Створіть {f}"


class TestCounts:
    @pytest.mark.parametrize("f,exp", EXPECTED.items())
    def test_count(self, f, exp):
        fp = _fp(f)
        if not os.path.isfile(fp): pytest.skip()
        assert len(_tests(fp)) >= exp, f"{f}: потрібно {exp} тестів"


class TestAsserts:
    @pytest.mark.parametrize("f", EXERCISE_FILES)
    def test_asserts(self, f):
        fp = _fp(f)
        if not os.path.isfile(fp): pytest.skip()
        missing = [t for t in _tests(fp) if not _has_assert(fp, t)]
        assert not missing, f"{f}: без assert: {', '.join(missing)}"


class TestPass:
    @pytest.mark.parametrize("f", EXERCISE_FILES)
    def test_pass(self, f):
        fp = _fp(f)
        if not os.path.isfile(fp): pytest.skip()
        assert pytest.main([fp, "-v", "--tb=short", "-q", "--no-header"]) == 0