# Вправи — Lesson 26: JUnit Report

У цій папці — практичні вправи до Lesson 26.
Усі вправи парсять готовий JUnit-XML рядок через `xml.etree.ElementTree`.
Реальний `pytest --junitxml` запускати НЕ потрібно.

## Файли

- `EXERCISES.md` — опис усіх завдань
- `exercise_1_parse.py` — вправа 1: підрахунок summary (tests/failures/skipped/passed)
- `exercise_2_summary.py` — вправа 2: побудова summary-рядка
- `exercise_3_fix_report.py` — вправа 3: знайти і виправити помилку в підрахунку
- `test_exercises.py` — автоматична перевірка

## Як працювати

1. Прочитайте завдання в `EXERCISES.md`
2. Замініть `pass` на правильний код (вправи 1-2)
3. Запустіть свій файл: `pytest exercise_1_parse.py -v`
4. Коли все зелене — запустіть перевірку: `pytest test_exercises.py -v`
