# Вправи — Lesson 26: Creating Functions

## 🏋️ Вправа 1: Прості функції (EASY)

| Функція | Що робить |
|---------|----------|
| `double(n)` | Повертає n * 2 |
| `greet(name)` | Повертає "Hello, {name}!" |
| `is_even(n)` | Повертає True якщо парне |

## 🏋️ Вправа 2: Helper-функції (MEDIUM)

| Функція | Що робить |
|---------|----------|
| `make_user(name, role)` | Повертає {"name": ..., "role": ..., "active": True} |
| `is_success_code(code)` | True якщо 200 <= code < 300 |
| `format_price(amount)` | Повертає "$X.XX" |

## 🏋️ Вправа 3: Валідація (MEDIUM)

| Функція | Що робить |
|---------|----------|
| `is_valid_email(email)` | email не порожній, містить "@" |
| `validate_password(pwd)` | >= 8 символів, є цифра |
| `is_valid_age(age)` | 0 <= age <= 150 |

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```