"""Приклад 3: API-тест (arrange-act-assert) + авторизація з env.
Запуск: pytest example_3_api_test.py -v"""
import os


class MockApiClient:
    """Фейковий клієнт: перевіряє заголовок Authorization перед видачею відповіді."""

    def __init__(self, responses, required_token=None):
        self._responses = responses
        self._required_token = required_token

    def get(self, path, headers=None):
        headers = headers or {}
        if self._required_token is not None:
            if headers.get("Authorization") != f"Bearer {self._required_token}":
                return {"status": 401, "json": {"error": "unauthorized"}}
        return self._responses.get(path, {"status": 404, "json": {}})


def build_auth_header():
    """Заголовок авторизації з токеном з оточення (НІКОЛИ не хардкодимо)."""
    token = os.getenv("API_TOKEN", "")
    return {"Authorization": f"Bearer {token}"}


def test_get_user_aaa():
    # arrange
    client = MockApiClient({"/users/1": {"status": 200, "json": {"id": 1, "name": "Alice"}}})
    # act
    resp = client.get("/users/1")
    # assert
    assert resp["status"] == 200
    assert resp["json"]["id"] == 1
    assert resp["json"]["name"] == "Alice"

def test_authorized_request(monkeypatch):
    # arrange — токен приходить з оточення (у тесті через monkeypatch)
    monkeypatch.setenv("API_TOKEN", "test-token-123")
    client = MockApiClient(
        {"/me": {"status": 200, "json": {"name": "Alice"}}},
        required_token="test-token-123",
    )
    # act
    resp = client.get("/me", headers=build_auth_header())
    # assert
    assert resp["status"] == 200
    assert resp["json"]["name"] == "Alice"

def test_missing_token_unauthorized(monkeypatch):
    # arrange — токена немає у оточенні
    monkeypatch.delenv("API_TOKEN", raising=False)
    client = MockApiClient({"/me": {"status": 200, "json": {}}}, required_token="test-token-123")
    # act
    resp = client.get("/me", headers=build_auth_header())
    # assert
    assert resp["status"] == 401
    assert resp["json"]["error"] == "unauthorized"
