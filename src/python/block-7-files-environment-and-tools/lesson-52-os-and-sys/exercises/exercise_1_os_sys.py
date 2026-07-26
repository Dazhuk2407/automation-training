"""Вправа 1: os та sys. Запуск: pytest exercise_1_os_sys.py -v

Реалізуй функції (прибери pass) і допиши asserts у тестах.
env vars у тестах став через fixture monkeypatch.
"""
import os
import sys


def get_env_or_default(key, default):
    # TODO: return os.getenv(key, default)
    pass


def get_config(key):
    # TODO: прочитай env var key, якщо немає — поверни None
    # TODO: return os.getenv(key)
    pass


def get_platform():
    # TODO: return sys.platform
    pass


def test_default_when_missing(monkeypatch):
    # TODO: monkeypatch.delenv("BASE_URL", raising=False)
    # TODO: assert get_env_or_default("BASE_URL", "http://localhost") == "http://localhost"
    pass


def test_value_from_env(monkeypatch):
    # TODO: monkeypatch.setenv("BASE_URL", "http://127.0.0.1:9000")
    # TODO: assert get_env_or_default("BASE_URL", "http://localhost") == "http://127.0.0.1:9000"
    pass


def test_config_missing_is_none(monkeypatch):
    # TODO: monkeypatch.delenv("API_TOKEN", raising=False)
    # TODO: assert get_config("API_TOKEN") is None
    pass


def test_config_from_env(monkeypatch):
    # TODO: monkeypatch.setenv("API_TOKEN", "abc123")
    # TODO: assert get_config("API_TOKEN") == "abc123"
    pass


def test_platform_is_str():
    # TODO: assert isinstance(get_platform(), str)
    pass
