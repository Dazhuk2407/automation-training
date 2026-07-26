# Вправи — Lesson 14: Fixture Best Practices

У цій папці знаходяться практичні вправи до Lesson 14.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `exercise_1_isolation.py` — вправа 1: ізоляція фікстур (замініть pass на assert)
- `exercise_2_refactor.py` — вправа 2: рефакторинг «комбайна» у малі композовані фікстури
- `exercise_3_fix_practice.py` — вправа 3: «виправ» — мутабельний спільний стан ламає ізоляцію
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. Замініть `pass` на правильний код (assert або `return`)
3. Запустіть свій файл: `pytest exercise_1_isolation.py -v`
4. У `exercise_3_fix_practice.py` спочатку один тест падає — виправте фікстуру за блоком `# ВІДПОВІДЬ`
5. Коли все зелене — запустіть перевірку: `pytest test_exercises.py -v`
