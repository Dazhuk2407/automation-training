"""
Приклад 3: Практичні сценарії в тестах.

Запуск: pytest example_3_practical.py -v
"""


def test_generate_test_ids():
    """range для генерації тестових ID."""
    user_ids = list(range(100, 105))
    assert len(user_ids) == 5
    assert user_ids[0] == 100


def test_pagination_offsets():
    """range для генерації offset-ів пагінації."""
    page_size = 25
    total = 100
    offsets = list(range(0, total, page_size))
    assert offsets == [0, 25, 50, 75]


def test_zip_input_expected():
    """zip для створення пар input/expected."""
    inputs = [200, 404, 500]
    expected_types = ["success", "client_error", "server_error"]

    for code, exp_type in zip(inputs, expected_types):
        if code < 400:
            actual = "success"
        elif code < 500:
            actual = "client_error"
        else:
            actual = "server_error"
        assert actual == exp_type


def test_enumerate_find_errors():
    """enumerate для пошуку індексів помилок."""
    responses = [200, 200, 404, 200, 500, 200]
    error_indices = [i for i, code in enumerate(responses) if code >= 400]
    assert error_indices == [2, 4]


def test_zip_build_users():
    """zip для побудови тестових даних."""
    names = ["Alice", "Bob", "Charlie"]
    roles = ["admin", "user", "user"]
    users = [{"name": n, "role": r} for n, r in zip(names, roles)]

    assert len(users) == 3
    assert users[0] == {"name": "Alice", "role": "admin"}