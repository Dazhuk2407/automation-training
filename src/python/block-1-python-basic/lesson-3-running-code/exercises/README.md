# Вправи - Lesson 3: Running code

## Завдання 1: Запустіть файл з термінала

Створіть файл `hello.py`:
```python
print("Running from terminal!")
```

Запустіть:
```bash
python3 hello.py
```

## Завдання 2: Запустіть з IDE

- [ ] Відкрийте файл в IDE
- [ ] Нажміть Run button
- [ ] Побачите результат у консолі

## Завдання 3: Файл з аргументами

Створіть `greet.py`:
```python
import sys
if len(sys.argv) > 1:
    print(f"Hello, {sys.argv[1]}!")
else:
    print("Hello, World!")
```

Запустіть:
```bash
python3 greet.py Alice
```

## Завдання 4: Інтерактивний режим

```bash
python3
>>> print("Welcome!")
>>> 2 + 2
4
>>> exit()
```

---

**✅ Коли вміс запускаються обома способами - переходьте до Lesson 4**
