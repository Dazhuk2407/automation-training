# Lesson 62: Writing Helper Scripts

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Писати маленькі повторно використовувані helper-функції
- ✅ Реалізувати типові утиліти: `chunk`, `flatten`, `retry`, `safe_get`
- ✅ Робити функції чистими (вхід → вихід) і легко тестованими
- ✅ Будувати власний «інструментальний пояс» автоматизатора
- ✅ Уникати `time.sleep` у юніт-тестах

---

## 📋 Передумови

Ви вже знаєте:
- Функції, `*args` / `**kwargs` (Lesson 30)
- Винятки та їх обробку (Lesson 35)
- Структури даних: list, dict, set (Block 2)

---

## 📖 Теорія

### 1. Що таке helper

Helper — це **маленька чиста функція**, яку перевикористовують у різних тестах.
«Чиста» означає: результат залежить лише від аргументів, немає прихованого стану
чи побічних ефектів (мережа, файли, глобальні змінні). Такі функції легко читати,
переиспользовувати й тестувати.

```python
def to_upper_list(items):
    """Повернути новий список у верхньому регістрі."""
    return [x.upper() for x in items]

to_upper_list(["a", "b"])  # ["A", "B"]
```

Правило: **одна функція — одна відповідальність**.

---

### 2. chunk(seq, n) — розбити список на частини по n

Часто треба обробити дані «пачками»: 100 користувачів по 10 за раз.

```python
def chunk(seq, n):
    """Розбити seq на шматки довжиною n."""
    return [seq[i:i + n] for i in range(0, len(seq), n)]

chunk([1, 2, 3, 4, 5], 2)   # [[1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4], 2)      # [[1, 2], [3, 4]]
```

Останній шматок може бути неповним — це нормально.

---

### 3. flatten(nested) — розгорнути на один рівень

```python
def flatten(nested):
    """Розгорнути вкладені списки на ОДИН рівень."""
    result = []
    for item in nested:
        result.extend(item)
    return result

flatten([[1, 2], [3], [4, 5]])   # [1, 2, 3, 4, 5]
flatten([["a"], ["b", "c"]])      # ["a", "b", "c"]
```

Тільки один рівень: `flatten([[1, [2]]])` → `[1, [2]]`.

---

### 4. retry(func, attempts) — повторити виклик

Нестабільні кроки (flaky) інколи падають випадково. `retry` повторює виклик,
поки не буде успіху або поки не вичерпаються спроби.

```python
def retry(func, attempts=3):
    """Викликати func до attempts разів, повернути перший успіх."""
    last = None
    for _ in range(attempts):
        try:
            return func()
        except Exception as e:
            last = e
    raise last
```

⚠️ У прикладах і тестах **без `time.sleep`** — інакше тести стають повільними й флакі.
Для тесту передають функцію, яка кидає задану кількість разів через лічильник.

---

### 5. safe_get(d, *keys) — безпечна навігація

Замість `d["a"]["b"]["c"]` (яке впаде на `KeyError`) — безпечний спуск:

```python
def safe_get(d, *keys, default=None):
    """Безпечно дістати значення з вкладеного dict."""
    cur = d
    for key in keys:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur

data = {"user": {"profile": {"name": "Alice"}}}
safe_get(data, "user", "profile", "name")   # "Alice"
safe_get(data, "user", "email")              # None
```

---

### 6. У QA automation

- **Генерація тест-даних:** `chunk` розбиває датасет на батчі, `flatten` збирає результати.
- **Повтор нестабільних кроків:** `retry` навколо крихких API-викликів.
- **Форматування:** `safe_get` дістає поля з JSON-відповіді, не боячись `KeyError`.

Ці утиліти живуть у `helpers.py` / `utils.py` і імпортуються в тести.

---

## ⚠️ Типові помилки

### Helper робить забагато

```python
# ❌ Одна функція читає файл, парсить і валідує
def process(path):
    data = open(path).read()
    parsed = parse(data)
    validate(parsed)
    return parsed

# ✅ Розділити на чисті функції з однією відповідальністю
def parse(text): ...
def validate(data): ...
```

### Прихований стан / побічні ефекти

```python
_cache = []

# ❌ Функція мутує глобальний стан
def add(x):
    _cache.append(x)
    return _cache

# ✅ Чиста функція — тільки вхід і вихід
def add(items, x):
    return items + [x]
```

### time.sleep у юніт-тестах

```python
# ❌ Повільно і флакі
def retry(func):
    for _ in range(3):
        try:
            return func()
        except Exception:
            time.sleep(1)

# ✅ У юніт-тестах sleep=0 або лічильник викликів без реального часу
```

### Ретраї без ліміту

```python
# ❌ Нескінченний цикл якщо func завжди падає
while True:
    try:
        return func()
    except Exception:
        pass

# ✅ Завжди обмежуй кількість спроб
for _ in range(attempts):
    ...
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-63-api-automation-intro`
