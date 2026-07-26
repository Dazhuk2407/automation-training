"""Приклад 1: common helpers. Запуск: pytest example_1_common_helpers.py -v"""


def chunk(seq, n):
    return [seq[i:i + n] for i in range(0, len(seq), n)]

def flatten(nested):
    result = []
    for item in nested:
        result.extend(item)
    return result

def unique(seq):
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def test_chunk():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert chunk([], 3) == []

def test_flatten():
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([["a"], ["b", "c"]]) == ["a", "b", "c"]
    assert flatten([]) == []

def test_flatten_one_level_only():
    assert flatten([[1, [2]], [3]]) == [1, [2], 3]

def test_unique_preserves_order():
    assert unique([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert unique(["a", "a", "b"]) == ["a", "b"]
    assert unique([]) == []
