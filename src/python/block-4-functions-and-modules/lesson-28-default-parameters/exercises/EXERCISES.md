# Вправи — Lesson 28: Default Parameters

## 🏋️ Вправа 1: Defaults (EASY)

| Функція | Default |
|---------|---------|
| `greet(name, greeting="Hello")` | greeting="Hello" |
| `make_config(host, port=8080, debug=False)` | port, debug |

## 🏋️ Вправа 2: Виправити mutable (MEDIUM)

Виправити функції що мають `def func(items=[])` → `def func(items=None)`.

## 🏋️ Вправа 3: Builder-функції (MEDIUM)

| Функція | Що робить |
|---------|----------|
| `create_user(name, role="user", tags=None)` | dict з user |
| `build_headers(token=None, content_type="application/json")` | dict headers |

## ✅ Перевірка: `pytest test_exercises.py -v`