# Приклади - Lesson 1: Install Python

## Команди для перевірки

```bash
# Перевірити версію Python
python3 --version
# Output: Python 3.11.5

# Перевірити версію pip
pip3 --version
# Output: pip 23.3 from /usr/local/lib/python3.11/site-packages/python (python 3.11)

# Дізнатися де встановлено Python
which python3
# Output: /usr/local/bin/python3

# Перевірити всю інформацію
python3 -c "import sys; print(sys.version)"
# Output: 3.11.5 (main, Feb 27 2025, 10:30:45)

# Дізнатися де знаходиться стандартна бібліотека
python3 -c "import sys; print(sys.prefix)"
# Output: /usr/local/opt/python@3.11/Frameworks/Python.framework/Versions/3.11
```

