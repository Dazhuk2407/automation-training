# Вправи — Lesson 22: break and continue

## 🏋️ Вправа 1: break (EASY)

**Файл:** `exercise_1_break.py`

| Тест | Що зробити |
|------|-----------|
| `test_find_first_error` | break на першому коді >= 400 |
| `test_find_user` | break коли знайшли "Bob" |
| `test_stop_at_limit` | break коли сума > 100 |

## 🏋️ Вправа 2: continue (EASY)

**Файл:** `exercise_2_continue.py`

| Тест | Що зробити |
|------|-----------|
| `test_skip_none` | continue для None |
| `test_only_positive` | continue для <= 0 |
| `test_valid_emails` | continue для невалідних email |

## 🏋️ Вправа 3: Комбіноване (MEDIUM)

**Файл:** `exercise_3_combined.py`

| Тест | Що зробити |
|------|-----------|
| `test_skip_and_stop` | continue для None, break для "STOP" |
| `test_else_all_ok` | else коли break не спрацював |
| `test_else_has_error` | else не виконується після break |

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```