# Вправи — Lesson 25: Stop on First Failure

У цій папці знаходяться практичні вправи до Lesson 25.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `exercise_1_stop.py` — вправа 1: логіка `-x` (== `--maxfail=1`)
- `exercise_2_maxfail.py` — вправа 2: логіка `--maxfail=N`
- `exercise_3_fix_stop.py` — вправа 3: знайти і виправити неправильний assert
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. Замініть `pass` на правильний `assert` (вправи 1-2)
3. Виправте зламаний тест (вправа 3)
4. Запустіть свій файл: `pytest exercise_1_stop.py -v`
5. Коли все зелене — запустіть перевірку: `pytest test_exercises.py -v`
