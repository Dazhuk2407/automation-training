"""
Приклад 3: Default параметри в реальних функціях.
Запуск: pytest example_3_real_world.py -v
"""


def create_user(name, role="user", active=True, permissions=None):
    if permissions is None:
        permissions = []
    return {"name": name, "role": role, "active": active, "permissions": permissions}


def build_headers(content_type="application/json", token=None):
    headers = {"Content-Type": content_type}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def test_user_defaults():
    user = create_user("Alice")
    assert user["role"] == "user"
    assert user["active"] is True
    assert user["permissions"] == []


def test_user_admin():
    user = create_user("Bob", role="admin", permissions=["read", "write"])
    assert user["role"] == "admin"
    assert user["permissions"] == ["read", "write"]


def test_users_independent_permissions():
    """Кожен user має свій список permissions."""
    u1 = create_user("Alice")
    u2 = create_user("Bob")
    u1["permissions"].append("admin")
    assert u2["permissions"] == []  # ✅ не зіпсований


def test_headers_default():
    headers = build_headers()
    assert headers == {"Content-Type": "application/json"}


def test_headers_with_token():
    headers = build_headers(token="abc123")
    assert headers["Authorization"] == "Bearer abc123"