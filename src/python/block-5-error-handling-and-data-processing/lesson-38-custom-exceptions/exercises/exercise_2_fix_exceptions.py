"""Вправа 2: виправ помилку. Запуск: pytest exercise_2_fix_exceptions.py -v

Деякі тести падають. Знайди баг (позначено # BUG:) і виправ його.
Після виправлення всі тести мають бути зеленими.
"""

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
        # BUG: піднімається не той виняток — має бути NetworkError, а не ConfigError
        raise ConfigError("connection refused")
    return f"connected to {host}"


def test_config_error():
    with pytest.raises(ConfigError) as exc:
        load_config({})
    assert "host" in str(exc.value)


def test_network_error():
    with pytest.raises(NetworkError) as exc:
        connect("")
    assert "refused" in str(exc.value)


def test_base_catches_all():
    with pytest.raises(AppError):
        connect("")
    assert issubclass(NetworkError, AppError)


def test_connect_ok():
    assert connect("api.com") == "connected to api.com"
