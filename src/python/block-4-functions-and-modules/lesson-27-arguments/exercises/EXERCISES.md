# Вправи — Lesson 27: Arguments

## 🏋️ Вправа 1: Positional та keyword (EASY)

| Тест | Що зробити |
|------|-----------|
| `test_positional` | create_user("Alice", "admin") |
| `test_keyword` | create_user(name="Alice", role="admin") |
| `test_reversed_keyword` | create_user(role="admin", name="Alice") |

## 🏋️ Вправа 2: Змішування (MEDIUM)

| Тест | Що зробити |
|------|-----------|
| `test_mixed_call` | Positional + keyword |
| `test_default_used` | Пропустити опціональний аргумент |
| `test_override_default` | Перевизначити default через keyword |

## 🏋️ Вправа 3: Helper-функції (MEDIUM)

Написати `assert_status(response, expected=200)` та `build_url(host, path, port=443)`.

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```