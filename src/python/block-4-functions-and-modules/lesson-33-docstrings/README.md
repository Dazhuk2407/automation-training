# Lesson 33: Docstrings

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Документувати функції через docstrings
- ✅ Використовувати one-line та multi-line docstrings
- ✅ Описувати параметри, return та винятки
- ✅ Розуміти `__doc__` та help()

---

## 📋 Передумови

Ви вже знаєте:
- Функції, аргументи, return (Lesson 26-29)

---

## 📖 Теорія

### 1. Що таке docstring

Docstring — рядок документації, перший рядок у функції/класі/модулі:

```python
def add(a, b):
    """Додати два числа."""
    return a + b

# Доступ через __doc__
print(add.__doc__)  # "Додати два числа."
```

---

### 2. One-line docstring

Для простих функцій:

```python
def is_even(n):
    """Повернути True якщо n парне."""
    return n % 2 == 0
```

**Правила:**
- Потрійні лапки навіть для одного рядка
- Крапка в кінці
- Дієслово в інфінітиві: "Повернути...", "Перевірити...", "Створити..."

---

### 3. Multi-line docstring (Google style)

```python
def create_user(name, role="user", active=True):
    """Створити словник користувача.

    Args:
        name: Ім'я користувача.
        role: Роль (за замовчуванням "user").
        active: Чи активний (за замовчуванням True).

    Returns:
        Словник з полями name, role, active.

    Raises:
        ValueError: Якщо name порожній.
    """
    if not name:
        raise ValueError("Name cannot be empty")
    return {"name": name, "role": role, "active": active}
```

---

### 4. Коли писати docstrings

| Ситуація | Потрібен docstring? |
|----------|-------------------|
| Публічна функція/API | ✅ Обов'язково |
| Helper для тестів | ✅ Короткий |
| Очевидна функція (`def add(a, b)`) | Бажано (one-line) |
| Внутрішня деталь (_private) | Опціонально |

---

### 5. Docstrings у тестах

```python
def test_login_success():
    """Перевірити успішний логін з валідними credentials."""
    response = login("alice", "password123")
    assert response["status"] == 200

def test_login_wrong_password():
    """Перевірити що неправильний пароль повертає 401."""
    response = login("alice", "wrong")
    assert response["status"] == 401
```

pytest показує docstring у verbose виводі: `PASSED - Перевірити успішний логін...`

---

## ⚠️ Типові помилки

### Коментар замість docstring

```python
# ❌ Це коментар — не видно через help()
def func():
    # Робить щось
    pass

# ✅ Docstring — доступний через __doc__
def func():
    """Робить щось."""
    pass
```

### Docstring що повторює код

```python
# ❌ Не інформативно
def add(a, b):
    """Додати a та b."""  # і так видно з коду

# ✅ Пояснює контекст
def add(a, b):
    """Додати два числа та повернути результат."""
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-34-imports`