# Lesson 15: Copying Data (Копіювання даних)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розуміти різницю між shallow copy та deep copy
- ✅ Використовувати `.copy()`, `list()`, `dict()` для shallow copy
- ✅ Використовувати `copy.deepcopy()` для вкладених структур
- ✅ Розуміти коли shallow copy недостатньо
- ✅ Безпечно копіювати тестові дані

---

## 📋 Передумови

Ви вже знаєте:
- Mutable vs immutable типи (Lesson 14)
- Чому `other = items` — це посилання, не копія
- Side effects при передачі mutable даних у функції

---

## 📖 Теорія

### 1. Проблема: присвоєння — це не копія

```python
original = [1, 2, 3]
not_a_copy = original    # ТОЙ САМИЙ об'єкт
not_a_copy.append(4)
# original = [1, 2, 3, 4] — зіпсований!
```

---

### 2. Shallow Copy (поверхнева копія)

Створює **новий контейнер**, але елементи всередині — ті самі об'єкти:

```python
# Для списків
original = [1, 2, 3]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

copy1.append(4)
# original = [1, 2, 3] — не змінився ✅

# Для словників
user = {"name": "Alice", "role": "admin"}
copy = user.copy()
copy["role"] = "user"
# user["role"] все ще "admin" ✅
```

---

### 3. Проблема shallow copy: вкладені об'єкти

Shallow copy копіює лише **перший рівень**. Вкладені об'єкти залишаються спільними:

```python
users = [
    {"name": "Alice", "scores": [90, 85]},
    {"name": "Bob", "scores": [70, 75]},
]

# Shallow copy — новий список, але ті самі словники всередині
copy = users.copy()

# Зміна вкладеного об'єкта впливає на обидва!
copy[0]["scores"].append(95)
# users[0]["scores"] = [90, 85, 95] — СЮРПРИЗ!
```

**Чому так?** `users.copy()` створив новий список, але словники `{"name": "Alice", ...}` всередині — ті самі об'єкти. Copy скопіював **посилання**, не самі словники.

---

### 4. Deep Copy (глибока копія)

`copy.deepcopy()` рекурсивно копіює **все** — включно з вкладеними об'єктами:

```python
import copy

users = [
    {"name": "Alice", "scores": [90, 85]},
    {"name": "Bob", "scores": [70, 75]},
]

deep = copy.deepcopy(users)

deep[0]["scores"].append(95)
# users[0]["scores"] = [90, 85] — оригінал чистий ✅
# deep[0]["scores"] = [90, 85, 95] — тільки копія змінилась
```

---

### 5. Коли що використовувати

| Ситуація | Спосіб | Чому |
|----------|--------|------|
| Плоский список `[1, 2, 3]` | `.copy()` або `[:]` | Немає вкладених об'єктів |
| Плоский dict `{"a": 1}` | `.copy()` або `{**d}` | Немає вкладених об'єктів |
| Вкладені структури | `copy.deepcopy()` | Вкладені об'єкти теж копіюються |
| Immutable дані (tuple, str) | Не потрібно копіювати | Не можна змінити |

**Правило:** якщо дані мають **один рівень вкладеності** — `.copy()` достатньо. Якщо є **вкладені list/dict** — використовуйте `deepcopy()`.

---

### 6. У тестах

```python
import copy


BASE_USER = {
    "name": "Alice",
    "roles": ["user"],
    "settings": {"theme": "light", "notifications": True},
}


def test_shallow_copy_problem():
    """Shallow copy — вкладені об'єкти спільні."""
    user = BASE_USER.copy()
    user["roles"].append("admin")
    # BASE_USER["roles"] тепер ["user", "admin"] — зіпсований!
    assert "admin" in BASE_USER["roles"]  # True — проблема


def test_deep_copy_safe():
    """Deep copy — повністю незалежна копія."""
    user = copy.deepcopy(BASE_USER)
    user["roles"].append("admin")
    assert "admin" not in BASE_USER["roles"]  # ✅ оригінал чистий
```

---

## ⚠️ Типові помилки

### Shallow copy для вкладених даних

```python
# ❌ Вкладений list спільний
data = {"items": [1, 2, 3]}
copy = data.copy()
copy["items"].append(4)
# data["items"] = [1, 2, 3, 4] — зіпсований!

# ✅ Deep copy
import copy
safe = copy.deepcopy(data)
```

### Забули import copy

```python
# ❌ NameError: name 'deepcopy' is not defined
# safe = deepcopy(data)

# ✅
import copy
safe = copy.deepcopy(data)
# або
from copy import deepcopy
safe = deepcopy(data)
```

### Зайве копіювання immutable

```python
# ❌ Безглуздо — рядки immutable
name = "Alice"
name_copy = copy.deepcopy(name)  # зайве

# ✅ Просто присвоєння
name_copy = name
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-16-range-and-zip`