# Приклади - Lesson 2: IDE Setup

## Як налаштувати IDE

### PyCharm

1. Завантажте PyCharm з [jetbrains.com](https://www.jetbrains.com/pycharm/download/)
2. Встановіть Community Edition
3. Створіть новий проект (не "Open", а саме "New Project")
4. File → Settings → Project → Python Interpreter
5. Додайте інтерпретатор

### VS Code

1. Завантажте VS Code з [code.visualstudio.com](https://code.visualstudio.com/)
2. Встановіть розширення "Python" від Microsoft
3. Ctrl+Shift+P (Cmd+Shift+P на macOS)
4. Пошукайте "Python: Select Interpreter"
5. Виберіть вашу версію Python
6. Перезапустіть VS Code, якщо інтерпретатор не застосувався

## Тестування

```python
# Створіть файл test.py
import sys

print("IDE works!")
print("Python version:", sys.version)
```

Запустіть з IDE за допомогою Run button або Ctrl+F10 (PyCharm) / F5 (VS Code)
