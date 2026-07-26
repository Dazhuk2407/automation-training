"""
Вправа 2: Кілька conftest-фікстур разом.

Один тест може попросити одразу кілька фікстур з conftest.py.
Використовуйте sample_user, app_config, test_data БЕЗ import.
Замініть pass на правильний assert.

Запуск: pytest exercise_2_combine.py -v
"""


def test_user_age(sample_user):
    """sample_user["age"] має дорівнювати 30."""
    # TODO: замініть pass на: assert sample_user["age"] == 30
    pass


def test_config_retries(app_config):
    """app_config["retries"] має дорівнювати 3."""
    # TODO: замініть pass на: assert app_config["retries"] == 3
    pass


def test_cart_contains_mouse(test_data):
    """"Mouse" має бути у test_data["cart"]."""
    # TODO: замініть pass на: assert "Mouse" in test_data["cart"]
    pass


def test_user_and_config_together(sample_user, app_config):
    """Один тест просить дві conftest-фікстури одночасно."""
    # TODO: замініть pass на дві перевірки:
    #   assert sample_user["role"] == "admin"
    #   assert app_config["timeout"] == 5
    pass


def test_all_three_fixtures(sample_user, app_config, test_data):
    """Три conftest-фікстури в одному тесті."""
    # TODO: замініть pass на три перевірки:
    #   assert sample_user["name"] == "Alice"
    #   assert app_config["base_url"] == "https://api.example.com"
    #   assert test_data["product"]["id"] == 42
    pass
