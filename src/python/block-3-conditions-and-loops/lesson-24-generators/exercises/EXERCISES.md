# Вправи — Lesson 24: Generators

## 🏋️ Вправа 1: Generator expressions (EASY)

| Тест | Що зробити |
|------|-----------|
| `test_all_positive` | all(n > 0 for n in numbers) |
| `test_any_error` | any(c >= 400 for c in codes) |
| `test_sum_gen` | sum через generator |

## 🏋️ Вправа 2: yield (MEDIUM)

| Тест | Що зробити |
|------|-----------|
| `test_count_up` | Написати генератор count_up(n) |
| `test_generate_ids` | Генератор ID від start до end |
| `test_page_numbers` | Генератор номерів сторінок |

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```