# Приклади - Lesson 10: Debugging

## Код для дебагування

```python
"""
Приклад кода для практики дебагування.
Поставте breakpoint на рядки з коментарями.
"""

def calculate_sum(numbers):
    """Обчислити суму списку."""
    total = 0  # 🔴 Breakpoint тут
    
    for num in numbers:  # 🔴 Breakpoint тут
        total += num
    
    return total


def process_data(data):
    """Обробити дані."""
    result = []
    
    for item in data:  # 🔴 Breakpoint тут
        processed = item * 2
        result.append(processed)
    
    return result


def main():
    """Головна функція."""
    numbers = [1, 2, 3, 4, 5]
    
    # Поставте breakpoint тут
    total = calculate_sum(numbers)  # 🔴 Breakpoint
    
    data = [10, 20, 30]
    processed = process_data(data)
    
    print(f"Total: {total}")
    print(f"Processed: {processed}")


if __name__ == "__main__":
    main()
```

## Інструкції для дебагування

1. Поставте breakpoint натиском на ліве поле
2. Запустіть Debug mode
3. Використайте:
   - F10: Step Over
   - F11: Step Into
   - Shift+F11: Step Out
