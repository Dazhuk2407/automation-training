# Вправи — Lesson 22: xfail

У цій папці знаходяться практичні вправи до Lesson 22.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `exercise_1_xfail.py` — вправа 1: базовий xfail (додати декоратор + assert)
- `exercise_2_conditions.py` — вправа 2: умовний xfail (дописати декоратор)
- `exercise_3_fix_xfail.py` — вправа 3: «виправ» падаючий тест з відомим багом
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. Виконайте TODO у файлах вправ
3. Запустіть свій файл: `pytest exercise_1_xfail.py -rxX -v`
4. Коли підсумок `0 failed` — запустіть перевірку: `pytest test_exercises.py -v`
