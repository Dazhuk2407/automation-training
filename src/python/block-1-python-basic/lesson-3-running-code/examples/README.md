# Приклади - Lesson 3: Running code

## Простий скрипт

```python
# hello.py
print("Hello, World!")
```

Запуск:
```bash
python3 hello.py
# Output: Hello, World!
```

## Скрипт з аргументами

```python
# greet.py
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("Hello, stranger!")
```

Запуск:
```bash
python3 greet.py Alice
# Output: Hello, Alice!
```

## Інтерактивний режим

```bash
python3
>>> x = 5
>>> y = 3
>>> print(x + y)
8
>>> exit()
```

## Запуск з IDE

У PyCharm або VS Code натисніть Run button 
або скористайтесь клавішами:
- PyCharm: Ctrl+Shift+F10
- VS Code: Ctrl+F5
