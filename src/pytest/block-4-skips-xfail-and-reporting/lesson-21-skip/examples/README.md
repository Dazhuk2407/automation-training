# Приклади — Lesson 21: Skip Tests

## Файли

- `example_1_mark_skip.py` — безумовний пропуск через `@pytest.mark.skip(reason=...)` + звичайні passing тести (5 тестів)
- `example_2_skipif.py` — умовний пропуск через `@pytest.mark.skipif(condition, reason=...)` (5 тестів)
- `example_3_imperative_skip.py` — імперативний `pytest.skip(...)` всередині тесту для динамічних умов (5 тестів)

## Як працювати

1. Запустіть кожен приклад:
   ```bash
   pytest example_1_mark_skip.py -v
   pytest example_2_skipif.py -v
   pytest example_3_imperative_skip.py -v
   ```
2. Зверніть увагу: у виводі будуть і `PASSED`, і `SKIPPED`.
   **Пропущені тести — це нормально, не падіння.** Exit code лишається `0`.
3. Подивіться причини пропусків прапорцем `-rs`:
   ```bash
   pytest example_1_mark_skip.py -rs
   ```
