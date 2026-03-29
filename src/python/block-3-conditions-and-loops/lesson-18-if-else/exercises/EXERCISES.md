# Вправи — Lesson 18: if / else

---

## 🏋️ Вправа 1: Класифікація (EASY)

**Файл:** `exercise_1_classify.py`

Допишіть функції та тести:

| Функція | Логіка |
|---------|--------|
| `classify_age(age)` | <13 → "child", <18 → "teen", <65 → "adult", else → "senior" |
| `classify_score(score)` | >=90 → "A", >=80 → "B", >=70 → "C", else → "F" |

---

## 🏋️ Вправа 2: Валідація (MEDIUM)

**Файл:** `exercise_2_validate.py`

| Функція | Логіка |
|---------|--------|
| `validate_password(pwd)` | порожній → "empty", <8 символів → "too_short", без цифр → "no_digit", else → "valid" |
| `validate_config(config)` | немає "host" → "missing_host", немає "port" → "missing_port", else → "valid" |

---

## 🏋️ Вправа 3: Truthy/Falsy (EASY)

**Файл:** `exercise_3_truthy.py`

| Тест | Що перевірити |
|------|--------------|
| `test_empty_list_falsy` | `not []` → True |
| `test_nonempty_truthy` | `bool([1])` → True |
| `test_none_falsy` | `not None` → True |
| `test_zero_falsy` | `not 0` → True |
| `test_string_truthy` | `bool("text")` → True |

---

## 🏋️ Вправа 4: Граничні значення (MEDIUM)

**Файл:** `exercise_4_boundaries.py`

Напишіть тести для boundary values функцій з Вправи 1.

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```