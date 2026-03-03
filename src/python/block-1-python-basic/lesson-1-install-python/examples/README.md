# Приклади - Lesson 1: Install Python

## Команди для перевірки

```bash
# Перевірити версію Python
python3 --version
# Output: Python 3.12.x

# Перевірити версію pip
pip3 --version
# Output: pip 23.3 from /usr/local/lib/python3.11/site-packages/python (python 3.11)

# Дізнатися де встановлено Python
which python3
# Output: /usr/local/bin/python3

# Перевірити всю інформацію
python3 -c "import sys; print(sys.version)"
# Output: 3.12.x (main, Feb 27 2025, 10:30:45)

# Дізнатися де знаходиться стандартна бібліотека
python3 -c "import sys; print(sys.prefix)"
# Output: /usr/local/opt/python@3.12/Frameworks/Python.framework/Versions/3.12
```

---

## Як запустити приклад скрипта `hello_world.py`

### Варіант 1: Запуск з кореня проєкту

```bash
python3 src/python/block-1-python-basic/lesson-1-install-python/examples/hello_world.py
```

### Варіант 2: Запуск з папки уроку

```bash
cd src/python/block-1-python-basic/lesson-1-install-python
python3 examples/hello_world.py
```

### Варіант 3: Запуск з папки examples

```bash
cd src/python/block-1-python-basic/lesson-1-install-python/examples
python3 hello_world.py
```

### Очікуваний результат

```text
Hello from Python!
Python version: 3.12.7
Project root: /Users/ivan.dazhuk/workspace/automation-training
```

**Примітка:** `Project root` може відрізнятися залежно від вашої системи та місця, де знаходиться проєкт.

