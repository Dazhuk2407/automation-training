# Вправи — Lesson 16: Data-Driven Testing

У цій папці знаходяться практичні вправи до Lesson 16.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `exercise_1_datasets.py` — вправа 1: винести дані в набір + parametrize
- `exercise_2_negative.py` — вправа 2: додати негативні кейси та `ids`
- `exercise_3_fix_data.py` — вправа 3: знайти й виправити неправильний кейс у наборі
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. Допишіть набори даних та замініть `pass` на правильний `assert`
3. Запустіть свій файл: `pytest exercise_1_datasets.py -v`
4. Коли все зелене — запустіть перевірку: `pytest test_exercises.py -v`
