"""
Приклад 2: Кілька спільних фікстур з conftest.py.

app_config, client та sample_user — усі з examples/conftest.py.
Один тест може попросити одразу кілька conftest-фікстур.

Запуск: pytest example_2_multiple_shared.py -v
"""


def test_config(app_config):
    """Фікстура config з conftest."""
    assert app_config["base_url"] == "https://api.example.com"
    assert app_config["timeout"] == 5


def test_client_uses_config(client):
    """client залежить від app_config — pytest збере ланцюжок сам."""
    assert client["base_url"] == "https://api.example.com"
    assert client["session_id"] == "abc-123"


def test_multiple_fixtures_together(sample_user, app_config, client):
    """Один тест просить три conftest-фікстури одночасно."""
    assert sample_user["role"] == "admin"
    assert app_config["timeout"] == 5
    assert client["session_id"] == "abc-123"
