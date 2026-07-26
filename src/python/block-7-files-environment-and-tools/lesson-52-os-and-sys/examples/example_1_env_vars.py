"""Приклад 1: env vars через os.getenv. Запуск: pytest example_1_env_vars.py -v"""
import os


def get_base_url():
    # Безпечний дефолт для локальної розробки
    return os.getenv("BASE_URL", "http://localhost")


def get_timeout():
    return int(os.getenv("TIMEOUT", "30"))


def get_token():
    # Секрет читаємо з env, без дефолту і без хардкоду
    return os.getenv("API_TOKEN")


def test_base_url_default():
    # env через monkeypatch, тут перевіряємо відсутність змінної
    assert get_base_url() == "http://localhost"


def test_base_url_from_env(monkeypatch):
    monkeypatch.setenv("BASE_URL", "http://127.0.0.1:8080")
    assert get_base_url() == "http://127.0.0.1:8080"


def test_timeout_default():
    assert get_timeout() == 30


def test_timeout_from_env(monkeypatch):
    monkeypatch.setenv("TIMEOUT", "5")
    assert get_timeout() == 5


def test_token_missing_is_none(monkeypatch):
    monkeypatch.delenv("API_TOKEN", raising=False)
    assert get_token() is None


def test_token_from_env(monkeypatch):
    monkeypatch.setenv("API_TOKEN", "test-token")
    assert get_token() == "test-token"
