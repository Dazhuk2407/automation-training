# Приклади — Lesson 5: Прості тести для базових типів

## Файли

- `example_1_numbers.py` — тести для int та float, pytest.approx (7 тестів)
- `example_2_strings.py` — тести для рядків: рівність, вміст, методи (6 тестів)
- `example_3_collections.py` — тести для list, dict, set, tuple (8 тестів)

## Як працювати

1. Перегляньте кожен файл — зверніть увагу на стиль: один тест = одна ідея
2. Запустіть:
   ```bash
   pytest example_1_numbers.py -v
   pytest example_2_strings.py -v
   pytest example_3_collections.py -v
   ```
3. Спробуйте змінити значення в `assert` щоб побачити як тест падає