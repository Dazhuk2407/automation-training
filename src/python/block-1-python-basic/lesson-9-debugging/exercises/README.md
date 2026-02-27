# Вправи - Lesson 10: Debugging

## Завдання 1: Поставте breakpoint

Створіть файл `debug_example.py`:

```python
def add(a, b):
    result = a + b  # 🔴 Поставте breakpoint тут
    return result

def main():
    x = 5
    y = 3
    total = add(x, y)  # 🔴 Поставте breakpoint тут
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
```

## Завдання 2: Запустіть Debug

1. Відкрийте файл в IDE
2. Натисніть на ліве поле рядка щоб поставити breakpoint
3. Запустіть Debug (F5 або меню)

## Завдання 3: Step Over та Step Into

1. Коли виконання паузується на breakpoint:
   - Нажміть F10 (Step Over) - перейти до наступного рядка
   - Нажміть F11 (Step Into) - увійти в функцію
   - Спостерігайте значення змінних

## Завдання 4: Variable Inspection

Під час дебагування:
1. Переглянути змінні в Variables панелі
2. Побачити типи даних
3. Побачити значення

## Завдання 5: Watch Expression

1. Додайте вираз для спостереження: `x + y`
2. Спостерігайте як змінюється значення

## Завдання 6: Call Stack

1. Переглянути Call Stack панель
2. Бачите порядок викликів функцій
3. Розумієте як програма дійшла до breakpoint

---

**✅ Коли дебагер працює правильно - переходьте до Lesson 11**
