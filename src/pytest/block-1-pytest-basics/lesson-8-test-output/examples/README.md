# Приклади — Lesson 8: Розуміння виводу pytest

## Файли

- `example_1_pass_and_fail.py` — passing тест + реально падаючий assert (1 passed, 1 failed)
- `example_2_runtime_errors.py` — помилки в коді: ZeroDivisionError, KeyError, TypeError (3 errors)
- `example_3_pytest_raises.py` — правильний спосіб тестувати винятки
- `example_4_print_output.py` — демонстрація print() з `-s` та без

## Як працювати

1. Запустіть `example_1` і прочитайте traceback:
   ```bash
   pytest example_1_pass_and_fail.py -v
   ```
2. Запустіть `example_2` з різним рівнем traceback:
   ```bash
   pytest example_2_runtime_errors.py --tb=short
   pytest example_2_runtime_errors.py --tb=no
   pytest example_2_runtime_errors.py -l
   ```
3. Порівняйте `example_2` (ERROR) з `example_3` (правильний підхід через pytest.raises)
4. Запустіть `example_4` з і без `-s`:
   ```bash
   pytest example_4_print_output.py
   pytest example_4_print_output.py -s
   ```