# Приклади — Lesson 6: Assertions

## Файли

- `example_1_basic_assertions.py` — базові assert: порівняння, boolean, типи, membership (6 тестів)
- `example_2_exceptions_and_approx.py` — pytest.raises та pytest.approx (5 тестів)
- `example_3_best_practices.py` — хороші та погані практики: introspection, messages, анти-патерни

## Як працювати

1. Запустіть кожен приклад:
   ```bash
   pytest example_1_basic_assertions.py -v
   pytest example_2_exceptions_and_approx.py -v
   ```
2. У `example_3_best_practices.py` є навмисно падаючий тест — запустіть і подивіться як pytest показує diff:
   ```bash
   pytest example_3_best_practices.py -v
   ```