# Приклади — Lesson 12: Python Typing

У цій папці знаходяться приклади до Lesson 12.

## Файли
- `example_1_basic_type_hints.py` — type hints для функцій та змінних (int, str, List, Dict, Tuple)
- `example_2_optional_union.py` — Optional (може бути None), Union (кілька типів)
- `example_3_complex_types.py` — Callable, вкладені типи, Dict[str, Any]

## Як працювати

1. Запустіть файл:
   ```bash
   python example_1_basic_type_hints.py
   ```
2. Подивіться результат
3. Спробуйте змінити типи та подивіться що зміниться
4. За бажанням перевірте файл через mypy:
   ```bash
   mypy example_1_basic_type_hints.py
   ```