# Приклади — Lesson 3: Перший тест у проєкті

Готовий міні-проєкт з тестами. Можна запустити і подивитись як все працює.

## Структура

```
examples/
├── src/
│   ├── __init__.py
│   └── calculator.py            # Код: add, subtract, multiply, divide
└── tests/
    ├── __init__.py
    ├── test_calculator.py       # Базові тести (4 тести)
    ├── test_edge_cases.py       # Edge cases: нуль, від'ємні (7 тестів)
    └── test_failing_demo.py     # Демо падаючого тесту (1 passed, 1 failed)
```

## Як працювати

1. Перегляньте `src/calculator.py` — це код який тестуємо
2. Перегляньте тести в `tests/`
3. Запустіть базові тести з папки `examples/`:
   ```bash
   cd examples
   pytest tests/test_calculator.py tests/test_edge_cases.py -v
   ```
4. Запустіть falling-тест для демонстрації:
   ```bash
   pytest tests/test_failing_demo.py -v
   ```
   Подивіться як pytest показує: який рядок впав, що очікувалось, що отримали.