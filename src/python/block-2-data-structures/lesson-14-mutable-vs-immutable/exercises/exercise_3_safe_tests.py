"""
Вправа 3: Безпечні тести без мутації спільних даних.
Запуск: pytest exercise_3_safe_tests.py -v
"""


def make_user():
    """Фабрика тестових даних."""
    return {"name": "Alice", "role": "user", "active": True}


BASE_CONFIG = {"host": "localhost", "port": 8080, "debug": False}


def test_modify_role():
    """Змінити role через фабрику — оригінал не зіпсується."""
    # TODO: замініть pass на:
    #   user = make_user()
    #   user["role"] = "admin"
    #   assert user["role"] == "admin"
    pass


def test_original_intact():
    """Фабрика дає свіжі дані кожен раз."""
    # TODO: замініть pass на:
    #   user = make_user()
    #   assert user["role"] == "user"
    pass


def test_config_override():
    """Створити test config через spread — оригінал не змінюється."""
    # TODO: замініть pass на:
    #   test_config = {**BASE_CONFIG, "debug": True, "port": 9090}
    #   assert test_config["debug"] is True
    #   assert BASE_CONFIG["debug"] is False
    pass


def test_list_extend_safe():
    """Розширити список без мутації оригіналу."""
    base = [1, 2, 3]
    # TODO: замініть pass на:
    #   extended = [*base, 4, 5]
    #   assert extended == [1, 2, 3, 4, 5]
    #   assert base == [1, 2, 3]
    pass