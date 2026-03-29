"""
Вправа 3: Helper-функції з аргументами.
Запуск: pytest exercise_3_helpers.py -v
"""


def assert_status(response, expected=200):
    """Перевірити статус response."""
    # TODO: замініть pass на: assert response["status"] == expected
    pass


def build_url(host, path, port=443):
    """Побудувати URL: https://{host}:{port}{path}."""
    # TODO: замініть pass на: return f"https://{host}:{port}{path}"
    pass


def test_assert_default_status():
    response = {"status": 200}
    # TODO: замініть pass на: assert_status(response)
    pass

def test_assert_custom_status():
    response = {"status": 201}
    # TODO: замініть pass на: assert_status(response, expected=201)
    pass

def test_build_url_default_port():
    # TODO: замініть pass на: assert build_url("api.com", "/users") == "https://api.com:443/users"
    pass

def test_build_url_custom_port():
    # TODO: замініть pass на: assert build_url("localhost", "/api", port=8080) == "https://localhost:8080/api"
    pass