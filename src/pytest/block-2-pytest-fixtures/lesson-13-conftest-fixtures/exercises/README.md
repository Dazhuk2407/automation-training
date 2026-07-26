# Вправи — Lesson 13: conftest.py

У цій папці знаходяться практичні вправи до Lesson 13.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `conftest.py` — спільні фікстури (`sample_user`, `app_config`, `test_data`)
- `exercise_1_use_conftest.py` — вправа 1: використання фікстур з conftest
- `exercise_2_combine.py` — вправа 2: кілька conftest-фікстур разом
- `exercise_3_fix_conftest.py` — вправа 3: «виправ» — один тест падає
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. Використовуйте фікстури з `conftest.py` **БЕЗ** import — просто як аргументи тестів
3. Замініть `pass` на правильний `assert`
4. Запустіть свій файл: `pytest exercise_1_use_conftest.py -v`
5. Коли все зелене — запустіть перевірку: `pytest test_exercises.py -v`
