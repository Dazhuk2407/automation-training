"""
Приклад 3: Формати набору даних — список dict і QA-таблиця тест-кейсів.

Список словників самодокументований, коли полів багато. Таблиця
тест-кейсів (шлях, метод, статус-код) — природний data-driven для QA.

Запуск: pytest example_3_data_structures.py -v
"""

import pytest


# ---- Логіка, яку перевіряємо ----

def is_adult(age):
    """Повнолітній з 18 років."""
    return age >= 18


def fake_request(path, method):
    """Імітація API: повертає статус-код для (шлях, метод)."""
    routes = {
        ("/users", "GET"): 200,
        ("/users/1", "GET"): 200,
        ("/users/9999", "GET"): 404,
        ("/users", "POST"): 201,
        ("/admin", "GET"): 403,
    }
    return routes.get((path, method), 404)


# ---- Список словників: самодокументовані дані ----

USER_CASES = [
    {"name": "Alice", "age": 30, "is_adult": True},
    {"name": "Bob", "age": 18, "is_adult": True},
    {"name": "Kid", "age": 15, "is_adult": False},
    {"name": "Baby", "age": 0, "is_adult": False},
]


@pytest.mark.parametrize("case", USER_CASES, ids=lambda c: c["name"])
def test_is_adult(case):
    """Ключі словника роблять дані читабельними прямо в наборі."""
    assert is_adult(case["age"]) is case["is_adult"]


# ---- QA-таблиця тест-кейсів: статус-коди API ----

API_CASES = [
    ("/users", "GET", 200),
    ("/users/1", "GET", 200),
    ("/users/9999", "GET", 404),
    ("/users", "POST", 201),
    ("/admin", "GET", 403),
]

API_IDS = [
    "list_ok",
    "get_ok",
    "not_found",
    "create_ok",
    "forbidden",
]


@pytest.mark.parametrize("path,method,status", API_CASES, ids=API_IDS)
def test_api_status(path, method, status):
    """Кожен рядок тест-плану = один рядок даних."""
    assert fake_request(path, method) == status
