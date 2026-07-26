"""Приклад 2: MockApiClient без мережі. Запуск: pytest example_2_mock_client.py -v"""


class MockApiClient:
    """Фейковий API-клієнт: повертає заздалегідь задані відповіді (dict зі status і json)."""

    def __init__(self, responses):
        self._responses = responses  # {"/users/1": {"status": 200, "json": {...}}}
        self.created = []

    def get(self, path):
        return self._responses.get(path, {"status": 404, "json": {}})

    def post(self, path, body):
        self.created.append((path, body))
        return {"status": 201, "json": body}


def test_get_known_path():
    client = MockApiClient({"/users/1": {"status": 200, "json": {"id": 1, "name": "Alice"}}})
    resp = client.get("/users/1")
    assert resp["status"] == 200
    assert resp["json"]["name"] == "Alice"

def test_get_unknown_path():
    client = MockApiClient({})
    resp = client.get("/users/999")
    assert resp["status"] == 404
    assert resp["json"] == {}

def test_post_creates():
    client = MockApiClient({})
    resp = client.post("/users", {"name": "Bob"})
    assert resp["status"] == 201
    assert resp["json"]["name"] == "Bob"
    assert client.created == [("/users", {"name": "Bob"})]
