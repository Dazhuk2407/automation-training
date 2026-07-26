"""Вправа 1: helpers. Запуск: pytest exercise_1_helpers.py -v"""


def chunk(seq, n):
    # TODO: return [seq[i:i + n] for i in range(0, len(seq), n)]
    pass

def flatten(nested):
    # TODO: розгорнути на один рівень (result.extend(item))
    pass

def safe_get(d, *keys, default=None):
    # TODO: пройти keys, повернути default якщо ключа немає
    pass

def test_chunk():
    # TODO: assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    pass

def test_chunk_empty():
    # TODO: assert chunk([], 3) == []
    pass

def test_flatten():
    # TODO: assert flatten([[1, 2], [3]]) == [1, 2, 3]
    pass

def test_safe_get_deep():
    # TODO: assert safe_get({"a": {"b": 1}}, "a", "b") == 1
    pass

def test_safe_get_missing():
    # TODO: assert safe_get({"a": {}}, "a", "x") is None
    pass
