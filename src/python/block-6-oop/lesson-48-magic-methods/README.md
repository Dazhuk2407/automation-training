# Lesson 48: Overview of Magic Methods (dunder)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розуміти що таке magic / dunder методи (`__name__`)
- ✅ Реалізувати `__str__` (для користувача) і `__repr__` (для розробника)
- ✅ Реалізувати `__eq__` для порівняння об'єктів за значенням
- ✅ Реалізувати `__len__` для власного контейнера
- ✅ Розуміти навіщо це у тестах (читабельні asserts, порівняння об'єктів)

---

## 📋 Передумови

Ви вже знаєте:
- Класи та об'єкти (Lesson 42)
- Конструктор `__init__` (Lesson 43)
- Наслідування (Lesson 46)

---

## 📖 Теорія

### 1. Що таке dunder-методи

**Dunder** (double underscore) або **magic** методи — це методи з подвійним підкресленням
навколо імені: `__init__`, `__str__`, `__len__`. Python **викликає їх неявно**, коли ви
використовуєте вбудований синтаксис: `print(obj)`, `len(obj)`, `obj1 == obj2`.

Ви вже бачили один такий метод — `__init__`, який Python викликає під час створення об'єкта:

```python
class User:
    def __init__(self, name):   # викликається неявно при User("Alice")
        self.name = name
```

Замість того щоб викликати ці методи напряму (`obj.__len__()`), ми пишемо звичний
синтаксис (`len(obj)`), а Python сам знаходить відповідний dunder-метод.

---

### 2. `__str__` vs `__repr__`

Обидва повертають рядок, але для різних цілей:

- `__str__` — **для користувача**. Викликається `str(obj)` і `print(obj)`. Читабельний.
- `__repr__` — **для розробника**. Викликається `repr(obj)`, показується у debug,
  в інтерактивній консолі та **всередині контейнерів** (list, dict).

```python
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User(name={self.name!r}, user_id={self.user_id})"


u = User("Alice", 1)
print(str(u))    # User: Alice          ← __str__
print(repr(u))   # User(name='Alice', user_id=1)  ← __repr__
print([u])       # [User(name='Alice', user_id=1)] ← контейнер бере __repr__
```

Якщо визначено тільки `__repr__`, він використовується і як fallback для `str()`.
Порада: якщо реалізуєте лише один — реалізуйте `__repr__`.

---

### 3. `__eq__` — порівняння `==`

Метод `__eq__` визначає поведінку оператора `==`. **Без нього** об'єкти порівнюються
за `id` (за адресою в пам'яті), тому два різні об'єкти з однаковими даними будуть **не рівні**:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Без __eq__:
Point(1, 2) == Point(1, 2)   # False! Порівняння за id
```

Додаємо `__eq__`, щоб порівнювати за значенням:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

Point(1, 2) == Point(1, 2)   # True! Порівняння за значенням
```

---

### 4. `__len__` — робить `len(obj)` робочим

Якщо ваш клас — це контейнер (обгортка над колекцією), реалізуйте `__len__`,
щоб працював вбудований `len()`:

```python
class TestSuite:
    def __init__(self, tests):
        self.tests = tests

    def __len__(self):
        return len(self.tests)

suite = TestSuite(["test_login", "test_logout", "test_signup"])
len(suite)   # 3
```

`__len__` **мусить повертати ціле невід'ємне число** (`int`).

---

### 5. Коротко про інші dunder-методи

Оглядово, для загального розуміння:

- `__lt__` / `__gt__` — визначають `<` / `>`, дозволяють **сортування** через `sorted()`
- `__contains__` — визначає оператор `in` (`x in obj`)
- `__getitem__` — дозволяє індексацію `obj[i]` і зріз `obj[1:3]`

```python
class Bag:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, index):
        return self.items[index]

bag = Bag(["a", "b", "c"])
"a" in bag     # True   ← __contains__
bag[0]         # "a"    ← __getitem__
```

---

### 6. Навіщо це у QA

Dunder-методи роблять тести **читабельними** та **потужними**:

- `__repr__` дає **інформативні повідомлення** при падінні assert. Порівняйте:

```python
# Без __repr__:
# assert user == expected
# E  assert <User object at 0x10a3f> == <User object at 0x10b21>   ← марно

# З __repr__:
# E  assert User(name='Alice', role='user') == User(name='Alice', role='admin')  ← видно різницю
```

- `__eq__` дозволяє **порівнювати об'єкти напряму** в assert:

```python
def test_parse_user():
    result = parse_user("Alice;admin")
    assert result == User("Alice", "admin")   # один зрозумілий рядок
```

---

## ⚠️ Типові помилки

### Плутати `__str__` і `__repr__`

```python
# ❌ __str__ з технічними деталями замість читабельності
def __str__(self):
    return f"<User object id={id(self)}>"

# ✅ __str__ — для людини, __repr__ — для розробника
def __str__(self):
    return f"User: {self.name}"

def __repr__(self):
    return f"User(name={self.name!r})"
```

### `__eq__` без узгодженого `__hash__`

Якщо ви визначаєте `__eq__`, Python робить об'єкт **unhashable** (не можна класти
в `set` чи ключем у `dict`). Якщо потрібна хешованість — додайте узгоджений `__hash__`:

```python
# ✅ хеш узгоджений з __eq__ (ті самі поля)
def __eq__(self, other):
    return self.x == other.x and self.y == other.y

def __hash__(self):
    return hash((self.x, self.y))
```

### Повертати не `str` зі `__str__`

```python
# ❌ TypeError: __str__ returned non-string
def __str__(self):
    return self.user_id      # int!

# ✅ завжди повертайте рядок
def __str__(self):
    return str(self.user_id)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-49-reading-writing-files`
