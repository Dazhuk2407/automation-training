# Lesson 32: Scope та Global Variables

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розуміти local, enclosing, global, built-in scope (LEGB)
- ✅ Розрізняти local та global змінні
- ✅ Використовувати `global` keyword (і розуміти чому рідко)
- ✅ Уникати shadowing та непередбачуваного стану

---

## 📋 Передумови

Ви вже знаєте:
- Функції, аргументи, return (Lesson 26-29)

---

## 📖 Теорія

### 1. LEGB правило

Python шукає змінну в такому порядку:

1. **L**ocal — всередині поточної функції
2. **E**nclosing — у зовнішній функції (для вкладених функцій)
3. **G**lobal — на рівні модуля
4. **B**uilt-in — вбудовані (len, print, range)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # "local" — L

    inner()
    print(x)  # "enclosing" — E

outer()
print(x)  # "global" — G
```

---

### 2. Local scope

Змінні створені всередині функції — локальні:

```python
def calculate():
    result = 42  # local
    return result

# print(result)  # NameError — result не існує поза функцією
```

---

### 3. Global keyword

`global` дозволяє змінити глобальну змінну зсередини функції:

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)  # 2
```

**Чому це погано:**
- Функція має побічний ефект — змінює стан поза собою
- Важко зрозуміти хто і коли змінює counter
- Важко тестувати

**Коли допустимо:** майже ніколи. Використовуйте return та параметри.

```python
# ❌ Global
counter = 0
def increment():
    global counter
    counter += 1

# ✅ Pure function
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)  # 1
counter = increment(counter)  # 2
```

---

### 4. Shadowing — затінення

```python
# ❌ Небезпечно: перезаписує вбудовану функцію
list = [1, 2, 3]
# list() тепер не працює!

# ❌ Небезпечно: local затінює параметр
def process(items):
    items = []  # створює LOCAL items, не змінює параметр
    return items

# ✅ Уникайте імен що збігаються з built-in
data = [1, 2, 3]
```

---

### 5. У тестах

```python
# ✅ Чисті функції — легко тестувати
def add_tax(price, tax_rate):
    return price * (1 + tax_rate)

def test_add_tax():
    assert add_tax(100, 0.2) == 120.0

# ❌ Global state — важко тестувати
TAX_RATE = 0.2
def add_tax_global(price):
    return price * (1 + TAX_RATE)
# Якщо хтось змінить TAX_RATE — тести зламаються
```

---

## ⚠️ Типові помилки

### UnboundLocalError

```python
x = 10
def func():
    # Python бачить присвоєння x = ... нижче і вважає x local
    print(x)  # UnboundLocalError!
    x = 20

# ✅ Або використовуйте інше ім'я, або передайте як параметр
```

### Shadowing built-in

```python
# ❌ Перезаписані built-in функції
list = [1, 2]    # list() більше не працює
dict = {"a": 1}  # dict() більше не працює
type = "user"    # type() більше не працює
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-33-docstrings`