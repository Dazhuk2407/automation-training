# Вправи — Lesson 4: Test Discovery

У цій папці знаходяться практичні вправи до Lesson 4.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `exercise_1_what_pytest_finds.py` — вправа 1: визначити що знайде pytest
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. Створіть файли у папці `my_project/` (вправи 2-6)
3. Використовуйте `pytest --collect-only` для перевірки
4. Запустіть автоматичну перевірку:
   ```bash
   pytest test_exercises.py -v
   ```