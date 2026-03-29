"""
Приклад 3: Аргументи у тестових helper-функціях.
Запуск: pytest example_3_in_tests.py -v
"""


def assert_response(response, status=200, has_data=True):
    """Універсальна валідація response."""
    assert response["status"] == status
    if has_data:
        assert "data" in response


def build_config(host="localhost", port=8080, debug=False):
    """Побудувати конфігурацію з defaults."""
    return {"host": host, "port": port, "debug": debug}


def test_assert_default():
    response = {"status": 200, "data": []}
    assert_response(response)


def test_assert_custom_status():
    response = {"status": 201, "data": {"id": 1}}
    assert_response(response, status=201)


def test_assert_no_data():
    response = {"status": 204}
    assert_response(response, status=204, has_data=False)


def test_config_default():
    config = build_config()
    assert config["host"] == "localhost"
    assert config["port"] == 8080


def test_config_custom():
    config = build_config(host="api.prod.com", port=443, debug=True)
    assert config["host"] == "api.prod.com"
    assert config["debug"] is True