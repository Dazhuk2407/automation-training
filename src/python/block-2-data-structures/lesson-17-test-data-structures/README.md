# Lesson 17: Робота зі складними тестовими даними

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Працювати з вкладеними структурами (dict + list)
- ✅ Парсити реальні API responses у тестах
- ✅ Безпечно навігувати по вкладених даних
- ✅ Писати перевірки для складних структур
- ✅ Створювати тестові дані для реальних сценаріїв

---

## 📋 Передумови

Ви вже знаєте:
- Всі структури даних: list, tuple, dict, set (Lesson 9-13)
- Mutable vs immutable, копіювання (Lesson 14-15)
- range(), zip(), enumerate() (Lesson 16)

Це фінальний урок Block 2 — він з'єднує все разом на реальних прикладах.

---

## 📖 Теорія

### 1. Реальні API responses — це вкладені структури

Типова відповідь REST API:

```python
response = {
    "status": 200,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@test.com", "roles": ["admin"]},
            {"id": 2, "name": "Bob", "email": "bob@test.com", "roles": ["user"]},
        ],
        "total": 2,
        "page": 1,
    },
}
```

Це **dict** → з вкладеним **dict** → з вкладеним **list** → з вкладеними **dict** → з вкладеними **list**. П'ять рівнів.

---

### 2. Навігація по вкладених даних

```python
# Крок за кроком
data = response["data"]           # dict
users = data["users"]             # list
first_user = users[0]             # dict
roles = first_user["roles"]       # list
first_role = roles[0]             # str → "admin"

# Або одним ланцюжком
name = response["data"]["users"][0]["name"]  # "Alice"
```

**Безпечна навігація:**

```python
# Якщо будь-який рівень може бути відсутній
users = response.get("data", {}).get("users", [])
if users:
    first_name = users[0].get("name", "Unknown")
```

---

### 3. Типові перевірки

```python
def test_response_status():
    assert response["status"] == 200

def test_users_count():
    users = response["data"]["users"]
    assert len(users) == 2

def test_first_user_is_admin():
    user = response["data"]["users"][0]
    assert "admin" in user["roles"]

def test_all_users_have_email():
    users = response["data"]["users"]
    for user in users:
        assert "email" in user
        assert "@" in user["email"]

def test_pagination():
    data = response["data"]
    assert data["total"] == 2
    assert data["page"] == 1
```

---

### 4. Фабрика тестових даних

Для складних структур — створюйте фабрику:

```python
import copy

BASE_RESPONSE = {
    "status": 200,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "roles": ["admin"]},
        ],
        "total": 1,
    },
}

def make_response(**overrides):
    """Створити response з можливістю перевизначення полів."""
    response = copy.deepcopy(BASE_RESPONSE)
    response.update(overrides)
    return response

def test_success():
    r = make_response()
    assert r["status"] == 200

def test_error():
    r = make_response(status=500)
    assert r["status"] == 500
```

---

### 5. List comprehension для фільтрації

```python
users = [
    {"name": "Alice", "active": True, "role": "admin"},
    {"name": "Bob", "active": False, "role": "user"},
    {"name": "Charlie", "active": True, "role": "user"},
]

# Активні користувачі
active = [u for u in users if u["active"]]
assert len(active) == 2

# Імена адмінів
admin_names = [u["name"] for u in users if u["role"] == "admin"]
assert admin_names == ["Alice"]

# Всі email (з .get для безпеки)
emails = [u.get("email", "N/A") for u in users]
```

---

### 6. Перевірка структури — патерн

```python
def validate_user(user):
    """Перевірити що user має правильну структуру."""
    required = ["id", "name", "email"]
    for field in required:
        assert field in user, f"Missing: {field}"
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert "@" in user.get("email", "")


def test_all_users_valid():
    users = response["data"]["users"]
    for user in users:
        validate_user(user)
```

---

## ⚠️ Типові помилки

### Довгий ланцюжок без перевірки

```python
# ❌ Будь-який KeyError/IndexError зламає все
name = response["data"]["users"][0]["profile"]["avatar"]["url"]

# ✅ Покроково з перевірками
data = response.get("data", {})
users = data.get("users", [])
if users:
    profile = users[0].get("profile", {})
    avatar = profile.get("avatar", {})
    url = avatar.get("url", "/default.png")
```

### Мутація тестових даних

```python
# ❌ Зміна вкладеного об'єкта зіпсує BASE
users = BASE_RESPONSE["data"]["users"]
users.append({"id": 3, "name": "New"})

# ✅ Deep copy
import copy
users = copy.deepcopy(BASE_RESPONSE["data"]["users"])
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Вітаємо! Ви завершили Block 2: Python Data Structures.**