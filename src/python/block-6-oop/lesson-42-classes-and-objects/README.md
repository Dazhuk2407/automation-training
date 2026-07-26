# Lesson 42: Classes and Objects

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Пояснити різницю між класом (шаблон) та об'єктом (екземпляр)
- ✅ Оголошувати клас через ключове слово `class`
- ✅ Створювати екземпляри класу
- ✅ Додавати атрибути та методи до класу
- ✅ Розуміти роль `self` у методах

---

## 📋 Передумови

Ви вже знаєте:
- Функції та параметри (Lesson 26-34)
- Словники як набір пар ключ-значення (прообраз об'єкта)

---

## 📖 Теорія

### 1. Клас vs об'єкт

**Клас** — це шаблон (креслення). **Об'єкт** (екземпляр) — конкретний виріб за цим кресленням.

Аналогія: клас `Car` — це креслення авто, а `my_car = Car()` — конкретна машина.

У QA: клас `TestCase` описує *що* таке тест-кейс, а кожен запуск створює свій екземпляр:

```python
class TestCase:
    pass

login_test = TestCase()   # один екземпляр
logout_test = TestCase()  # інший екземпляр
# один клас — багато об'єктів
```

---

### 2. Найпростіший клас

`pass` — порожнє тіло. Дужки `()` після імені створюють екземпляр:

```python
class Dog:
    pass

d = Dog()
print(type(d))            # <class '__main__.Dog'>
print(isinstance(d, Dog)) # True
```

---

### 3. Атрибути екземпляра

Атрибут — це змінна, що належить об'єкту. Доступ через крапку `obj.attr`:

```python
class Dog:
    def set_name(self, name):
        self.name = name  # присвоюємо атрибут екземпляру

d = Dog()
d.set_name("Rex")
print(d.name)  # Rex

# Атрибут можна задати і ззовні:
d.age = 3
print(d.age)   # 3
```

---

### 4. Методи і `self`

**Метод** — це функція всередині класу. Перший параметр завжди `self` — це посилання
на сам об'єкт, через яке метод читає та змінює його атрибути:

```python
class Counter:
    def reset(self):
        self.value = 0

    def increment(self):
        self.value += 1  # self дає доступ до стану об'єкта

c = Counter()
c.reset()
c.increment()
c.increment()
print(c.value)  # 2
```

Виклик `c.increment()` Python перетворює на `Counter.increment(c)` — тому `self` це `c`.

---

### 5. Кілька екземплярів незалежні

Кожен об'єкт має власний стан. Зміна одного не впливає на інший:

```python
class Counter:
    def reset(self):
        self.value = 0

    def increment(self):
        self.value += 1

a = Counter(); a.reset()
b = Counter(); b.reset()

a.increment()
a.increment()
b.increment()

print(a.value)  # 2
print(b.value)  # 1 — незалежний стан
```

---

### 6. У QA: об'єкт як обгортка стану

Клас зручно тримає разом дані та поведінку. Приклад — простий `ApiClient`
(поки без `__init__` — конструктор буде у Lesson 43):

```python
class ApiClient:
    def configure(self, base_url):
        self.base_url = base_url

    def get_status(self, path):
        # умовна логіка: збираємо повну URL і повертаємо "код"
        url = self.base_url + path
        return 200 if url.startswith("https://") else 500

client = ApiClient()
client.configure("https://api.example.com")
print(client.get_status("/health"))  # 200
```

---

## ⚠️ Типові помилки

### Забути `self` у методі

```python
class Dog:
    # ❌ немає self — Python передасть об'єкт у name
    # def set_name(name):
    #     self.name = name

    # ✅ перший параметр — self
    def set_name(self, name):
        self.name = name
```

### Плутати клас і екземпляр

```python
class Dog:
    def bark(self):
        return "woof"

# ❌ виклик методу на класі без екземпляра
# Dog.bark()        # TypeError: missing 'self'

# ✅ спершу створюємо об'єкт
d = Dog()
d.bark()            # "woof"
```

### Спільний стан там, де мав бути окремий

```python
class Cart:
    def add(self, item):
        # ✅ окремий список у кожного об'єкта
        if not hasattr(self, "items"):
            self.items = []
        self.items.append(item)

# два кошики — два незалежних списки
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-43-constructor-init`
