# Вправи — Lesson 19: Conditional Expressions

---

## 🏋️ Вправа 1: Тернарний оператор (EASY)

**Файл:** `exercise_1_ternary.py`

| Тест | Що зробити |
|------|-----------|
| `test_status_label` | "ok" if 200, else "error" |
| `test_adult_or_minor` | "adult" if age >= 18 else "minor" |
| `test_plural` | "test" if count == 1 else "tests" |
| `test_sign` | "positive" if n > 0, "zero" if n == 0, else "negative" |

---

## 🏋️ Вправа 2: or для defaults (EASY)

**Файл:** `exercise_2_or_defaults.py`

| Тест | Що зробити |
|------|-----------|
| `test_name_or_default` | `name or "Anonymous"` |
| `test_none_fallback` | `None or "fallback"` |
| `test_empty_string_fallback` | `"" or "default"` |

---

## 🏋️ Вправа 3: Практичні функції (MEDIUM)

**Файл:** `exercise_3_practical.py`

| Функція | Логіка |
|---------|--------|
| `display_name(user)` | nickname або name |
| `format_count(n)` | "1 item" або "N items" |
| `access_level(user)` | "full" if admin else "read-only" |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```