"""Приклад 2: retry. Запуск: pytest example_2_retry.py -v"""
import pytest


def retry(func, attempts=3):
    last = None
    for _ in range(attempts):
        try:
            return func()
        except Exception as e:
            last = e
    raise last

def test_retry_succeeds_first_time():
    assert retry(lambda: "ok") == "ok"

def test_retry_succeeds_on_second():
    calls = {"n": 0}
    def flaky():
        calls["n"] += 1
        if calls["n"] < 2:
            raise ValueError("fail")
        return "ok"
    assert retry(flaky) == "ok"
    assert calls["n"] == 2

def test_retry_exhausts_and_raises():
    calls = {"n": 0}
    def always_fails():
        calls["n"] += 1
        raise RuntimeError("boom")
    with pytest.raises(RuntimeError):
        retry(always_fails, attempts=3)
    assert calls["n"] == 3
