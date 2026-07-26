# Приклади — Lesson 17: Markers

## Файли

- `conftest.py` — реєструє власні маркери (`api`, `ui`, `critical`) через `pytest_configure`
- `example_1_builtin_markers.py` — готові маркери: `smoke`, `regression`, `slow` (4 тести)
- `example_2_custom_markers.py` — власні маркери: `api`, `ui`, `critical` (4 тести)
- `example_3_multiple_markers.py` — кілька маркерів на тесті, маркер на класі та файлі (`pytestmark`)

## Як працювати

1. Запустіть кожен приклад — усі тести проходять (маркер не змінює результат):
   ```bash
   pytest example_1_builtin_markers.py -v
   pytest example_2_custom_markers.py -v
   pytest example_3_multiple_markers.py -v
   ```
2. Спробуйте вибірковий запуск за маркером:
   ```bash
   pytest example_1_builtin_markers.py -m smoke -v
   pytest example_2_custom_markers.py -m api -v
   ```
3. Подивіться список зареєстрованих маркерів:
   ```bash
   pytest --markers
   ```

> У кореневому `pytest.ini` увімкнено `--strict-markers`. Власні маркери
> реєструються у `conftest.py` — без цього збір впав би з помилкою.
