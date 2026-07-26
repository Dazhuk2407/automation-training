"""Вправа 2: виправ баг. Запуск: pytest exercise_2_fix_helpers.py -v

Одна з функцій нижче містить баг (позначено `# BUG:`).
Знайди його, виправ — і всі test_* мають проходити.
Рівно один тест зараз падає.
"""
import pytest


def chunk(seq, n):
    # BUG: range зупиняється зарано і губить останній неповний шматок
    return [seq[i:i + n] for i in range(0, len(seq) - n + 1, n)]

def flatten(nested):
    result = []
    for item in nested:
        result.extend(item)
    return result

def retry(func, attempts=3):
    last = None
    for _ in range(attempts):
        try:
            return func()
        except Exception as e:
            last = e
    raise last

def test_chunk_full():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

def test_chunk_partial_last():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

def test_flatten():
    assert flatten([[1, 2], [3]]) == [1, 2, 3]

def test_retry_exhausts():
    def always_fails():
        raise ValueError("fail")
    with pytest.raises(ValueError):
        retry(always_fails, attempts=2)
    assert retry(lambda: 7) == 7
