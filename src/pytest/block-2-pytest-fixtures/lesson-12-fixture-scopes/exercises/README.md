# Вправи — Lesson 12: Fixture Scopes

У цій папці знаходяться практичні вправи до Lesson 12.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `exercise_1_scope.py` — вправа 1: function scope (default) та лічильник setup
- `exercise_2_shared_state.py` — вправа 2: module scope і спільний мутабельний стан
- `exercise_3_fix_scope.py` — вправа 3: виправте неправильний scope
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. У вправах 1-2 замініть `pass` на правильний `assert`
3. У вправі 3 знайдіть і виправте неправильний scope
4. Запустіть свій файл: `pytest exercise_1_scope.py -v`
5. Коли все зелене — запустіть перевірку: `pytest test_exercises.py -v`
