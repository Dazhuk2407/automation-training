"""
Приклад 3: Безпечне копіювання тестових даних.

Запуск: pytest example_3_tests_safe_data.py -v
"""

import copy


BASE_RESPONSE = {
    "status": 200,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "roles": ["admin"]},
            {"id": 2, "name": "Bob", "roles": ["user"]},
        ]
    },
}


def get_response():
    """Фабрика — deepcopy кожен раз."""
    return copy.deepcopy(BASE_RESPONSE)


def test_modify_response_safely():
    """Модифікація копії не зіпсує оригінал."""
    response = get_response()
    response["data"]["users"][0]["roles"].append("superuser")
    assert "superuser" not in BASE_RESPONSE["data"]["users"][0]["roles"]


def test_fresh_response_each_time():
    """Кожен виклик фабрики — свіжі дані."""
    r1 = get_response()
    r2 = get_response()
    r1["status"] = 500
    assert r2["status"] == 200


def test_override_status():
    """Створити response з іншим статусом."""
    response = get_response()
    response["status"] = 404
    assert response["status"] == 404
    assert BASE_RESPONSE["status"] == 200