"""Приклад 2: конфіг як dict. Запуск: pytest example_2_config.py -v

Конфіг проєкту — це просто словник налаштувань. Тут показано, як читати
значення з дефолтом і як зливати базовий конфіг з override.
"""


def get_setting(config, key, default=None):
    return config.get(key, default)

def merge_config(base, override):
    result = dict(base)
    result.update(override)
    return result

def test_get_setting_present():
    config = {"host": "localhost", "port": 8080}
    assert get_setting(config, "host") == "localhost"

def test_get_setting_default():
    config = {"host": "localhost"}
    assert get_setting(config, "port", 8080) == 8080

def test_merge_config():
    base = {"host": "localhost", "port": 8080, "debug": False}
    override = {"port": 9090, "debug": True}
    merged = merge_config(base, override)
    assert merged == {"host": "localhost", "port": 9090, "debug": True}

def test_merge_does_not_mutate_base():
    base = {"port": 8080}
    merge_config(base, {"port": 9090})
    assert base == {"port": 8080}
