"""
Приклад 2: continue — пропуск ітерації.
Запуск: pytest example_2_continue.py -v
"""


def test_skip_none():
    """Пропустити None значення."""
    data = [1, None, 2, None, 3]
    clean = []
    for item in data:
        if item is None:
            continue
        clean.append(item)
    assert clean == [1, 2, 3]


def test_skip_invalid_emails():
    """Пропустити невалідні email."""
    users = [
        {"name": "Alice", "email": "alice@test.com"},
        {"name": "Bob", "email": ""},
        {"name": "Charlie", "email": "charlie@test.com"},
        {"name": "Diana"},
    ]
    valid_emails = []
    for user in users:
        email = user.get("email", "")
        if not email or "@" not in email:
            continue
        valid_emails.append(email)
    assert valid_emails == ["alice@test.com", "charlie@test.com"]


def test_skip_negative():
    """Обробити тільки позитивні числа."""
    numbers = [-3, 5, -1, 8, 0, 12]
    positive_sum = 0
    for n in numbers:
        if n <= 0:
            continue
        positive_sum += n
    assert positive_sum == 25


def test_continue_does_not_stop():
    """continue не зупиняє цикл — тільки пропускає ітерацію."""
    count = 0
    for i in range(10):
        if i % 2 == 0:
            continue
        count += 1
    assert count == 5  # 1, 3, 5, 7, 9