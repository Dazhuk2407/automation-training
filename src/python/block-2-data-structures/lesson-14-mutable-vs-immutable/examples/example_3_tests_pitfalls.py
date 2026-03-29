"""
Приклад 3: Пастки мутабельності в тестах.

Запуск: pytest example_3_tests_pitfalls.py -v
"""


# --- Правильний підхід: фабрика ---

def make_user():
    """Фабрика — кожен виклик повертає свіжий dict."""
    return {"name": "Alice", "role": "user", "active": True}


def test_modify_user_role():
    """Змінюємо role — оригінал не зіпсується."""
    user = make_user()
    user["role"] = "admin"
    assert user["role"] == "admin"


def test_user_still_fresh():
    """Новий виклик make_user — свіжі дані."""
    user = make_user()
    assert user["role"] == "user"  # ✅ не "admin"


# --- Правильний підхід: spread оператор ---

def test_create_modified_copy():
    """Створити модифіковану копію без side effect."""
    base_config = {"host": "localhost", "port": 8080, "debug": False}
    test_config = {**base_config, "debug": True, "port": 9090}

    assert base_config["debug"] is False  # оригінал не змінився
    assert test_config["debug"] is True
    assert test_config["port"] == 9090


# --- Правильний підхід: list spread ---

def test_list_spread():
    """Новий список через spread."""
    base = [1, 2, 3]
    extended = [*base, 4, 5]

    assert base == [1, 2, 3]       # оригінал чистий
    assert extended == [1, 2, 3, 4, 5]