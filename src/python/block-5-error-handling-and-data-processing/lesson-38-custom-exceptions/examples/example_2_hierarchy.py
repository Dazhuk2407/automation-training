"""Приклад 2: ієрархія винятків. Запуск: pytest example_2_hierarchy.py -v"""

import pytest


class AppError(Exception):
    """Базовий виняток застосунку."""
    pass


class ConfigError(AppError):
    """Помилка конфігурації."""
    pass


class NetworkError(AppError):
    """Помилка мережі."""
    pass


def load_config(config):
    if "host" not in config:
        raise ConfigError("missing host")
    return config


def connect(host):
    if not host:
        raise NetworkError("connection refused")
    return f"connected to {host}"


def test_config_error():
    with pytest.raises(ConfigError):
        load_config({})


def test_network_error():
    with pytest.raises(NetworkError):
        connect("")


def test_base_catches_config():
    # Ловля базового класу перехоплює похідний ConfigError
    with pytest.raises(AppError):
        load_config({})


def test_base_catches_network():
    # Той самий except AppError ловить і NetworkError
    with pytest.raises(AppError):
        connect("")


def test_derived_is_subclass():
    assert issubclass(ConfigError, AppError)
    assert issubclass(NetworkError, AppError)


def test_catch_base_handles_all():
    caught = []
    for action in (lambda: load_config({}), lambda: connect("")):
        try:
            action()
        except AppError as e:
            caught.append(str(e))
    assert caught == ["missing host", "connection refused"]
