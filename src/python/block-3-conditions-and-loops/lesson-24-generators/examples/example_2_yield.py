"""
Приклад 2: Generator functions з yield.
Запуск: pytest example_2_yield.py -v
"""


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


def even_numbers(limit):
    n = 0
    while n < limit:
        yield n
        n += 2


def fibonacci(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def test_count_up():
    assert list(count_up_to(5)) == [1, 2, 3, 4, 5]


def test_even_numbers():
    assert list(even_numbers(10)) == [0, 2, 4, 6, 8]


def test_fibonacci():
    assert list(fibonacci(7)) == [0, 1, 1, 2, 3, 5, 8]


def test_generator_in_for():
    result = []
    for n in count_up_to(3):
        result.append(n * 10)
    assert result == [10, 20, 30]