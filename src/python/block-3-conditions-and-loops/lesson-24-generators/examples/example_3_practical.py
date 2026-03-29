"""
Приклад 3: Практичні генератори для тестів.
Запуск: pytest example_3_practical.py -v
"""


def generate_users(count):
    for i in range(1, count + 1):
        yield {"id": i, "name": f"User_{i}", "email": f"user{i}@test.com"}


def page_numbers(total, page_size):
    page = 1
    while (page - 1) * page_size < total:
        yield page
        page += 1


def retry_codes(codes):
    for code in codes:
        yield code


def test_generate_users():
    users = list(generate_users(3))
    assert len(users) == 3
    assert users[0]["name"] == "User_1"
    assert users[2]["email"] == "user3@test.com"


def test_pagination():
    pages = list(page_numbers(total=25, page_size=10))
    assert pages == [1, 2, 3]


def test_pagination_exact():
    pages = list(page_numbers(total=20, page_size=10))
    assert pages == [1, 2]


def test_retry_simulation():
    codes = list(retry_codes([500, 502, 200]))
    first_success = next((c for c in codes if c == 200), None)
    assert first_success == 200