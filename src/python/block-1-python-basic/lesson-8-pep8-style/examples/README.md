# Приклади — Lesson 8: PEP 8 and Code Formatting

У цій папці знаходяться приклади до Lesson 8.

## Файли
- `example_1_pep8_basic.py` — базові правила PEP 8: назви, пробіли, відступи
- `example_2_formatting_tools.py` — приклади форматування коду за допомогою `black`
- `example_3_linting.py` — приклади помилок, які знаходять `flake8` та `pylint`

## Як запускати
Запустіть будь-який приклад командою:

```bash
python example_1_pep8_basic.py
python example_2_formatting_tools.py
python example_3_linting.py

## Правильний код (PEP 8 compliant)

```python
"""
Модуль для роботи зі змінними.
"""

# Константи
MAX_ATTEMPTS = 3
DEFAULT_TIMEOUT = 30


def calculate_average(values):
    """Обчислити середнє значення списку.

    Args:
        values: Список чисел

    Returns:
        Середнє значення
    """
    total = sum(values)
    count = len(values)
    return total / count if count > 0 else 0


class DataProcessor:
    """Процесор для обробки даних."""

    def __init__(self, name):
        self.name = name
        self.data = []

    def add_data(self, value):
        """Додати значення."""
        self.data.append(value)

    def process(self):
        """Обробити дані."""
        return calculate_average(self.data)


if __name__ == "__main__":
    processor = DataProcessor("demo")
    processor.add_data(10)
    processor.add_data(20)
    print(processor.process())
```

## Неправильний код (порушення PEP 8)

```python
# ❌ Відступи змішані
def bad_function():
  x=1
   y=2  # Неправильний відступ
	z=3  # Tab замість пробілів

# ❌ Назвування
def MyFunction():  # PascalCase замість snake_case
    MyVariable=10  # Має бути my_variable
    CONSTANT_VALUE=20  # Немає пробілів навколо оператора =

# ❌ Пробіли
x=y+1  # Немає пробілів навколо операторів
def func(a,b,c = 1):  # не коректно коли немає пробілів
    pass
```
