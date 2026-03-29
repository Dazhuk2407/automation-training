"""
Приклад 3: Реальні сценарії — API response, config defaults.

Запуск: pytest example_3_real_world.py -v
"""


# --- Config з defaults ---

def get_config():
    """Імітація: файл конфігурації може мати не всі поля."""
    return {"host": "api.example.com", "debug": True}


def test_config_with_defaults():
    """Конфіг з default values для відсутніх полів."""
    config = get_config()
    host = config.get("host", "localhost")
    port = config.get("port", 8080)
    timeout = config.get("timeout", 30)
    debug = config.get("debug", False)

    assert host == "api.example.com"  # є в конфігу
    assert port == 8080               # default
    assert timeout == 30              # default
    assert debug is True              # є в конфігу


# --- API response з опціональними полями ---

def get_user_response():
    """Імітація API: деякі поля можуть бути відсутні."""
    return {
        "id": 1,
        "name": "Alice",
        "role": "admin",
        # "email" — відсутній
        # "avatar" — відсутній
    }


def test_required_fields_present():
    """Обов'язкові поля перевіряємо через []."""
    user = get_user_response()
    assert user["id"] == 1
    assert user["name"] == "Alice"


def test_optional_fields_safe():
    """Опціональні поля перевіряємо через .get()."""
    user = get_user_response()
    assert user.get("email") is None
    assert user.get("avatar", "/default.png") == "/default.png"


def test_build_display_name():
    """Побудувати display name з наявних даних."""
    user = get_user_response()
    nickname = user.get("nickname", user["name"])
    assert nickname == "Alice"  # fallback на name