# Вправи — Lesson 21: Skip Tests

У цій папці знаходяться практичні вправи до Lesson 21.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `exercise_1_skip.py` — вправа 1: безумовний `@pytest.mark.skip`
- `exercise_2_skipif.py` — вправа 2: умовний `@pytest.mark.skipif`
- `exercise_3_fix_skip.py` — вправа 3: виправ пропуск (один тест падає)
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. Допишіть `assert` або додайте skip-декоратор — за завданням
3. Запустіть свій файл: `pytest exercise_1_skip.py -v`
4. Памʼятайте: `SKIPPED` — це не помилка. Мета — **0 failures**.
5. Коли все зелене — запустіть перевірку: `pytest test_exercises.py -v`
