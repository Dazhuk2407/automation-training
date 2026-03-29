# Lesson 22: break and continue

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Використовувати `break` для виходу з циклу
- ✅ Використовувати `continue` для пропуску ітерації
- ✅ Розуміти `else` у циклах
- ✅ Обирати правильний інструмент для контролю циклу

---

## 📋 Передумови

Ви вже знаєте:
- for та while цикли (Lesson 20-21)

---

## 📖 Теорія

### 1. break — зупинити цикл

`break` повністю припиняє виконання циклу:

```python
def find_first_error(codes):
    """Знайти перший код помилки."""
    for code in codes:
        if code >= 400:
            return code  # break через return
    return None

# Або з break
for code in [200, 200, 404, 500]:
    if code >= 400:
        print(f"Found error: {code}")
        break
```

---

### 2. continue — пропустити ітерацію

`continue` пропускає решту тіла циклу і переходить до наступної ітерації:

```python
def get_valid_emails(users):
    """Зібрати тільки валідні email."""
    emails = []
    for user in users:
        if not user.get("email"):
            continue  # пропустити user без email
        if "@" not in user["email"]:
            continue  # пропустити невалідний email
        emails.append(user["email"])
    return emails
```

---

### 3. else у циклах

`else` виконується тільки якщо цикл завершився **без break**:

```python
def find_admin(users):
    """Знайти admin, або повідомити що немає."""
    for user in users:
        if user["role"] == "admin":
            return user
    else:
        return None  # цикл завершився без break/return

# Практичний приклад
def has_error(codes):
    for code in codes:
        if code >= 400:
            break
    else:
        return False  # жодної помилки
    return True  # знайшли помилку
```

---

### 4. break vs continue vs return

| Інструмент | Що робить | Коли використовувати |
|-----------|-----------|---------------------|
| `break` | Виходить з циклу | Знайшли що шукали |
| `continue` | Пропускає ітерацію | Цей елемент не підходить |
| `return` | Виходить з функції | Знайшли результат |

---

### 5. У тестах

```python
def test_break_on_first_error():
    """break зупиняє на першій помилці."""
    codes = [200, 200, 404, 500, 200]
    first_error = None
    for code in codes:
        if code >= 400:
            first_error = code
            break
    assert first_error == 404  # саме 404, не 500


def test_continue_skips_invalid():
    """continue пропускає невалідні дані."""
    data = [1, "skip", 2, None, 3]
    numbers = []
    for item in data:
        if not isinstance(item, int):
            continue
        numbers.append(item)
    assert numbers == [1, 2, 3]


def test_else_no_break():
    """else виконується коли break не спрацював."""
    codes = [200, 201, 204]
    all_ok = False
    for code in codes:
        if code >= 400:
            break
    else:
        all_ok = True
    assert all_ok is True
```

---

## ⚠️ Типові помилки

### break замість continue

```python
# ❌ break зупиняє весь цикл
for item in items:
    if not valid(item):
        break  # решта items не обробиться!

# ✅ continue пропускає тільки поточний
for item in items:
    if not valid(item):
        continue  # наступний item обробиться
```

### Забули що else у циклі — не як в if

```python
# else в циклі виконується коли break НЕ спрацював
# Це НЕ "інакше якщо цикл порожній"
for item in []:
    pass
else:
    print("Виконається!")  # так, виконається — break не було
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-23-list-comprehensions`