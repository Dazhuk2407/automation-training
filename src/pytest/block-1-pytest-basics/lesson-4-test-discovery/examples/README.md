# Приклади — Lesson 4: Test Discovery

## Файли

- `example_1_correct_naming.py` — правильні та неправильні назви функцій (pytest знайде тільки 3 з 6)
- `example_2_test_classes.py` — групування тестів у класи (2 класи, 6 тестів)
- `example_3_invisible_tests.py` — тести, які pytest НЕ знайде (`0 items collected`)
- `example_4_collect_only.sh` — скрипт для демонстрації `--collect-only`

## Як працювати

1. Запустіть `example_1` — у виводі мають бути тільки `test_addition`, `test_subtraction`, `test_string_upper`:
   ```bash
   pytest example_1_correct_naming.py -v
   ```
2. Запустіть `example_3` — має показати **`no tests collected`** (0 тестів), бо всі назви неправильні:
   ```bash
   pytest example_3_invisible_tests.py -v
   ```
3. Спробуйте `--collect-only` для порівняння:
   ```bash
   pytest --collect-only example_1_correct_naming.py
   pytest --collect-only example_3_invisible_tests.py
   ```

## Зверніть увагу

- `conftest.py` — спеціальний файл pytest. Він **не підкоряється** звичайному naming rule для тестових файлів (`test_*.py`). Pytest підхоплює його автоматично за назвою.