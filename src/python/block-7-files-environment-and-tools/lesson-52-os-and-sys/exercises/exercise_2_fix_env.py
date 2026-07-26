"""Вправа 2: виправ помилку. Запуск: pytest exercise_2_fix_env.py -v

Один тест падає. Знайди баг (позначено # BUG:) і виправ його.
Після виправлення всі тести мають бути зеленими.
"""
import os


def get_base_url():
    return os.getenv("BASE_URL", "http://localhost")


def get_timeout():
    # BUG: коли змінної немає, os.environ[...] кидає KeyError замість дефолту.
    #      Треба безпечно читати з дефолтом "30".
    return int(os.environ["TIMEOUT"])


def get_token():
    return os.getenv("API_TOKEN")


def test_base_url_default(monkeypatch):
    monkeypatch.delenv("BASE_URL", raising=False)
    assert get_base_url() == "http://localhost"


def test_timeout_default(monkeypatch):
    monkeypatch.delenv("TIMEOUT", raising=False)
    assert get_timeout() == 30


def test_timeout_from_env(monkeypatch):
    monkeypatch.setenv("TIMEOUT", "5")
    assert get_timeout() == 5


def test_token_from_env(monkeypatch):
    monkeypatch.setenv("API_TOKEN", "test-token")
    assert get_token() == "test-token"
