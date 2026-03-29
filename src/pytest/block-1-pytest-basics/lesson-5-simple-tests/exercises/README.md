# Вправи — Lesson 5: Прості тести для базових типів

У цій папці знаходяться практичні вправи до Lesson 5.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `exercise_1_numbers.py` — вправа 1: тести для чисел
- `exercise_2_strings.py` — вправа 2: тести для рядків
- `exercise_3_collections.py` — вправа 3: тести для списків та словників
- `exercise_4_float.py` — вправа 4: порівняння float
- `exercise_5_edge_cases.py` — вправа 5: edge cases
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. Відкрийте файл вправи
3. Замініть `pass` на `assert` (кожен TODO показує що саме)
4. Запустіть свій файл:
   ```bash
   pytest exercise_1_numbers.py -v
   ```
5. Коли все зелене — запустіть перевірку:
   ```bash
   pytest test_exercises.py -v
   ```

## Принцип

Один тест — одна ідея. Не пишіть один великий тест на все.