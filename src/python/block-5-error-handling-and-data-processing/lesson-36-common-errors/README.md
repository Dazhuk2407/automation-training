# Lesson 36: Common Python Errors

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розпізнавати поширені винятки: `ValueError`, `TypeError`, `KeyError`, `IndexError`, `AttributeError`, `NameError`, `ZeroDivisionError`
- ✅ Розуміти **чому** кожен з них виникає
- ✅ Відтворювати і перехоплювати їх у коді та тестах
- ✅ Уникати їх грамотним, захищеним кодом
- ✅ Ловити **конкретний** виняток замість загального

---

## 📋 Передумови

Ви вже знаєте:
- `try` / `except` / `finally` (Lesson 35)
- Структури даних: list, dict, tuple (Lesson 9-16)

---

## 📖 Теорія

Виняток (exception) — це подія, яка перериває нормальне виконання коду.
Python має багато **вбудованих** типів винятків, і кожен сигналізує про
конкретну проблему. Знати їх «в обличчя» — базова навичка QA-інженера:
саме ці помилки найчастіше видно у трейсбеках тестів.

### 1. ValueError — правильний тип, неправильне значення

Виникає, коли тип аргументу коректний, але саме **значення** не підходить:

```python
int("abc")     # ❌ ValueError: invalid literal for int() with base 10: 'abc'
int("42")      # ✅ 42 — рядок, але з валідним числом

int("12.5")    # ❌ ValueError — це float у рядку, не int
```

Безпечно обробити:

```python
def safe_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default

safe_int("42")    # 42
safe_int("abc")   # 0
```

---

### 2. TypeError — несумісні типи

Виникає, коли операція застосована до **невідповідного типу**:

```python
"a" + 1        # ❌ TypeError: can only concatenate str (not "int") to str
len(5)         # ❌ TypeError: object of type 'int' has no len()
None + 3       # ❌ TypeError: unsupported operand type(s)
```

Уникнути — явним приведенням типу:

```python
"a" + str(1)   # ✅ "a1"
len(str(5))    # ✅ 1
```

---

### 3. KeyError — відсутній ключ у dict

Виникає при зверненні до ключа, якого немає у словнику:

```python
user = {"name": "Alice"}
user["age"]    # ❌ KeyError: 'age'
```

Безпечна альтернатива — метод `.get()` (повертає `None` або default замість падіння):

```python
user.get("age")         # None — без винятку
user.get("age", 0)      # 0 — свій default
```

---

### 4. IndexError — індекс поза межами list

Виникає, коли індекс виходить за межі списку:

```python
nums = [10, 20, 30]
nums[5]        # ❌ IndexError: list index out of range
nums[-4]       # ❌ IndexError — від'ємний індекс теж за межами
```

Безпечно — перевірити довжину або впіймати виняток:

```python
def safe_index(items, i, default=None):
    if 0 <= i < len(items):
        return items[i]
    return default
```

---

### 5. AttributeError — метод/атрибут, якого немає

Виникає при зверненні до атрибута, якого в об'єкта немає.
Дуже часта причина — об'єкт виявився `None`:

```python
None.foo()     # ❌ AttributeError: 'NoneType' object has no attribute 'foo'
"x".append("y")  # ❌ AttributeError: 'str' object has no attribute 'append'
```

Уникнути — перевіркою на `None` перед зверненням:

```python
result = None
if result is not None:
    result.foo()   # ✅ викликаємо лише коли є об'єкт
```

---

### 6. NameError — використання невизначеної змінної

Виникає, коли змінна не була визначена — часто через **друкарську помилку**:

```python
print(usename)  # ❌ NameError: name 'usename' is not defined (мали на увазі username)
```

Уникнути — визначити змінну до використання й перевіряти назви:

```python
username = "Alice"
print(username)  # ✅
```

---

### 7. ZeroDivisionError — ділення на нуль

Виникає при діленні (або `%`) на нуль:

```python
10 / 0         # ❌ ZeroDivisionError: division by zero
10 % 0         # ❌ ZeroDivisionError: integer division or modulo by zero
```

Уникнути — перевіркою дільника:

```python
def safe_divide(a, b, default=0):
    if b == 0:
        return default
    return a / b
```

---

## ⚠️ Типові помилки

### Ловити всі помилки замість конкретної

```python
# ❌ занадто широко — приховає навіть баги в коді
try:
    value = int(text)
except Exception:
    value = 0

# ✅ ловимо саме той виняток, який очікуємо
try:
    value = int(text)
except ValueError:
    value = 0
```

### Ігнорувати винятки мовчки

```python
# ❌ помилка «проковтнута», ніхто не дізнається що зламалось
try:
    do_something()
except Exception:
    pass

# ✅ хоча б залогувати або обробити свідомо
try:
    do_something()
except ValueError as e:
    print(f"Помилка обробки: {e}")
```

### Звертатися до dict[key] без перевірки

```python
# ❌ впаде з KeyError якщо ключа немає
age = user["age"]

# ✅ безпечно через .get() з default
age = user.get("age", 0)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-37-reading-tracebacks`
