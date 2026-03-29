# Lesson 34: Python Import System

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Імпортувати модулі через `import` та `from ... import`
- ✅ Використовувати aliases (`as`)
- ✅ Організовувати імпорти за PEP 8
- ✅ Розуміти чому `import *` — погано

---

## 📋 Передумови

Ви вже знаєте:
- Функції та модулі (Lesson 26-33)
- Структуру проєкту з src/ та tests/

---

## 📖 Теорія

### 1. import module

```python
import os
import json
import math

# Використання через ім'я модуля
path = os.path.join("/home", "user")
data = json.loads('{"key": "value"}')
pi = math.pi
```

---

### 2. from module import name

```python
from os.path import join, exists
from json import loads, dumps
from math import pi, sqrt

# Використання напряму (без префіксу)
path = join("/home", "user")
data = loads('{"key": "value"}')
```

---

### 3. Aliases (as)

```python
import numpy as np              # стандартний alias
import pandas as pd
from datetime import datetime as dt

# Корисно для довгих імен
from collections import defaultdict as dd
```

---

### 4. Порядок імпортів (PEP 8)

```python
# 1. Стандартна бібліотека
import os
import json
from pathlib import Path

# 2. Сторонні пакети (pip install)
import pytest
import requests

# 3. Локальні модулі
from src.helpers import validate_email
from src.config import BASE_URL
```

Три групи, розділені порожнім рядком.

---

### 5. Чому `import *` — погано

```python
# ❌ Імпортує ВСЕ з модуля
from os.path import *

# Проблеми:
# 1. Не зрозуміло звідки функція: join() — це os.path.join? чи str.join?
# 2. Може перезаписати ваші змінні
# 3. IDE не може підказати
# 4. Читач коду не бачить залежності

# ✅ Імпортуйте конкретно
from os.path import join, exists
```

---

### 6. Практичні паттерни

```python
# Для тестів
import pytest
from src.calculator import add, subtract

# Для конфігурації
import os
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///test.db")

# Для helper-модуля
from typing import Optional, List
```

---

### 7. У тестах

```python
import pytest
from src.auth import authenticate, AuthError


def test_auth_success():
    result = authenticate("admin", "password123")
    assert result["status"] == "success"


def test_auth_failure():
    with pytest.raises(AuthError):
        authenticate("admin", "wrong")
```

---

## ⚠️ Типові помилки

### import * у production коді

```python
# ❌ Ніколи не робіть так
from module import *

# ✅ Конкретні імпорти
from module import function_a, function_b
```

### Circular imports

```python
# ❌ module_a імпортує module_b, module_b імпортує module_a
# ImportError або AttributeError

# ✅ Реструктуруйте код — виділіть спільне в третій модуль
```

### Невикористані імпорти

```python
# ❌ import є, але не використовується — засмічує код
import os
import json  # ніде не використовується

# ✅ Видаліть невикористане
import os
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Вітаємо! Ви завершили Block 4: Functions and Modules.**