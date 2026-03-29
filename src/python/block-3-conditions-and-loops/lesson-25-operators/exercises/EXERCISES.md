# Вправи — Lesson 25: Operators

## 🏋️ Вправа 1: Арифметичні (EASY)

| Тест | Що перевірити |
|------|--------------|
| `test_floor_division` | 10 // 3 == 3 |
| `test_modulo` | 10 % 3 == 1 |
| `test_power` | 2 ** 8 == 256 |
| `test_chained` | 1 < 5 < 10 |

## 🏋️ Вправа 2: Логічні (EASY)

| Тест | Що перевірити |
|------|--------------|
| `test_and` | True and True |
| `test_or` | False or True |
| `test_in_list` | 3 in [1,2,3] |
| `test_is_none` | None is None |
| `test_is_not_equality` | [1] == [1] but [1] is not [1] |

## 🏋️ Вправа 3: У тестах (MEDIUM)

| Тест | Що зробити |
|------|-----------|
| `test_status_range` | 200 <= code < 300 |
| `test_has_access` | role == "admin" and active |
| `test_even_number` | n % 2 == 0 |
| `test_augmented` | x += 10; x *= 2 |

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```