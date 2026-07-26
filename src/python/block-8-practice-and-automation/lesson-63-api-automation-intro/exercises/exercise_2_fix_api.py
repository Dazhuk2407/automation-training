"""Вправа 2: виправ баг. Запуск: pytest exercise_2_fix_api.py -v

Знайди рядок з `# BUG:` та виправ його так, щоб усі тести проходили.
Рівно один тест зараз падає.
"""


def status_class(code):
    return f"{code // 100}xx"

def is_success(code):
    # BUG: помилково зараховує 4xx як успіх (має бути 200 <= code < 300)
    return 200 <= code < 500

def get_user_name(response):
    return response["json"]["name"]


def test_status_class():
    assert status_class(503) == "5xx"

def test_is_success_ok():
    assert is_success(200) is True

def test_is_success_client_error():
    assert is_success(404) is False

def test_get_user_name():
    response = {"status": 200, "json": {"id": 1, "name": "Alice"}}
    assert get_user_name(response) == "Alice"
