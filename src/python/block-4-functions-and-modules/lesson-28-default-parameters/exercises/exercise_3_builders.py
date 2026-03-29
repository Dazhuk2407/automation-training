"""Вправа 3: Builder-функції. Запуск: pytest exercise_3_builders.py -v"""


def create_user(name, role="user", tags=None):
    # TODO: замініть pass на:
    #   if tags is None:
    #       tags = []
    #   return {"name": name, "role": role, "tags": tags}
    pass

def build_headers(token=None, content_type="application/json"):
    # TODO: замініть pass на:
    #   headers = {"Content-Type": content_type}
    #   if token:
    #       headers["Authorization"] = f"Bearer {token}"
    #   return headers
    pass

def test_user_default():
    # TODO: замініть pass на:
    #   u = create_user("Alice")
    #   assert u["role"] == "user"
    #   assert u["tags"] == []
    pass

def test_user_with_tags():
    # TODO: замініть pass на:
    #   u = create_user("Bob", role="admin", tags=["vip"])
    #   assert u["tags"] == ["vip"]
    pass

def test_headers_default():
    # TODO: замініть pass на:
    #   h = build_headers()
    #   assert h == {"Content-Type": "application/json"}
    pass

def test_headers_with_token():
    # TODO: замініть pass на:
    #   h = build_headers(token="abc")
    #   assert "Authorization" in h
    pass