"""
Вправа 1: Використання фікстур з conftest.py.

Фікстури sample_user, app_config, test_data оголошені у exercises/conftest.py.
Використовуйте їх БЕЗ import — просто додайте як аргумент тесту.
Замініть pass на правильний assert.

Запуск: pytest exercise_1_use_conftest.py -v
"""


def test_user_name(sample_user):
    """sample_user["name"] має дорівнювати "Alice"."""
    # TODO: замініть pass на: assert sample_user["name"] == "Alice"
    pass


def test_user_role(sample_user):
    """sample_user["role"] має дорівнювати "admin"."""
    # TODO: замініть pass на: assert sample_user["role"] == "admin"
    pass


def test_config_base_url(app_config):
    """app_config["base_url"] має дорівнювати "https://api.example.com"."""
    # TODO: замініть pass на: assert app_config["base_url"] == "https://api.example.com"
    pass


def test_config_timeout(app_config):
    """app_config["timeout"] має дорівнювати 5."""
    # TODO: замініть pass на: assert app_config["timeout"] == 5
    pass


def test_product_price(test_data):
    """test_data["product"]["price"] має дорівнювати 9.99."""
    # TODO: замініть pass на: assert test_data["product"]["price"] == 9.99
    pass
