# Приклади — Lesson 7: Запуск тестів з CLI

## Файли

- `example_1_cli_basics.py` — тести для демонстрації базових CLI-команд (5 тестів)
- `example_2_filtering.py` — тести з різними назвами для демонстрації `-k` фільтрації (6 тестів)
- `example_3_markers_preview.py` — короткий приклад маркерів `-m` (4 тести)

## Як працювати

Запустіть кожен приклад різними способами і порівняйте вивід:

```bash
# Базовий запуск
pytest example_1_cli_basics.py -v

# Тихий вивід
pytest example_1_cli_basics.py -q

# З print()
pytest example_1_cli_basics.py -s

# Фільтр за назвою
pytest example_2_filtering.py -k "login" -v
pytest example_2_filtering.py -k "not slow" -v

# Маркери
pytest example_3_markers_preview.py -m fast -v

# Подивитися що знайде pytest
pytest --collect-only
```