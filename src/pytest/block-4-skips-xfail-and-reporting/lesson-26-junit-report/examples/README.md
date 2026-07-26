# Приклади — Lesson 26: JUnit Report

У цій папці — приклади парсингу JUnit XML **готового рядка** через `xml.etree.ElementTree`.
Реальний `pytest --junitxml` тут НЕ запускається — ми працюємо з підготовленим XML-рядком,
щоб зосередитись на розумінні структури та підрахунку результатів.

## Файли

- `example_1_junit_format.py` — структура JUnit XML і підрахунок summary (tests/failures/skipped/passed)
- `example_2_parse_report.py` — розбір окремих `<testcase>`: імена всіх та імена впалих тестів
- `example_3_summary.py` — побудова summary-рядка `Tests: 4, Passed: 2, Failed: 1, Skipped: 1`

## Запуск

```bash
pytest example_1_junit_format.py -v
pytest example_2_parse_report.py -v
pytest example_3_summary.py -v
```
