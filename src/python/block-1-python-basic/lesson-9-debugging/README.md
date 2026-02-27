# Lesson 10: Basic debugging in IDE

## 🎯 Learning Outcomes

- ✅ Використовувати `print()` для debugging
- ✅ Ставити breakpoints в IDE
- ✅ Покроково виконувати код (Step Over, Step Into, Step Out)
- ✅ Інспектувати змінні під час виконання
- ✅ Розуміти call stack
- ✅ Знаходити та виправляти помилки

---

## 📖 Теорія

### 1. Print Debugging (Простий спосіб)

Найпростіший спосіб debugging - використання `print()`:

```python
def calculate_discount(price, discount_percent):
    print(f"🔍 DEBUG: price = {price}")  # Перевірка вхідних даних
    print(f"🔍 DEBUG: discount_percent = {discount_percent}")
    
    discount = price * (discount_percent / 100)
    print(f"🔍 DEBUG: discount = {discount}")  # Проміжний результат
    
    final_price = price - discount
    print(f"🔍 DEBUG: final_price = {final_price}")  # Фінальний результат
    
    return final_price

# Виклик функції
result = calculate_discount(1000, 20)
print(f"✅ Result: {result}")
```

**Переваги print debugging:**
- ✅ Простий та швидкий
- ✅ Працює скрізь
- ✅ Не потребує IDE

**Недоліки:**
- ❌ Засмічує код
- ❌ Треба видаляти після
- ❌ Не зручний для великих проектів

---

### 2. Breakpoints (Точки зупину)

Breakpoint - це мітка в коді, де виконання зупиниться.

**Як поставити breakpoint:**

#### PyCharm:
1. Клікніть на ліве поле рядка коду
2. З'явиться червона точка 🔴
3. Запустіть Debug (Shift+F9)

#### VS Code:
1. Клікніть на ліве поле рядка коду
2. З'явиться червона точка 🔴
3. Запустіть Debug (F5)

```python
def calculate(x, y):
    result = x + y  # 🔴 Поставте breakpoint тут
    return result * 2
```

---

### 3. Step Execution (Покрокове виконання)

Коли виконання зупинилось на breakpoint:

| Команда | Клавіша | Дія |
|---------|---------|-----|
| **Step Over** | F10 | Виконати поточний рядок, перейти до наступного |
| **Step Into** | F11 | Увійти в функцію (якщо рядок викликає функцію) |
| **Step Out** | Shift+F11 | Вийти з поточної функції |
| **Resume** | F9 | Продовжити до наступного breakpoint |

**Приклад:**

```python
def multiply(a, b):
    return a * b  # Якщо зробити Step Into, зайдете сюди

def calculate(x, y):
    result = multiply(x, y)  # 🔴 Breakpoint тут
    return result + 10       # F10 - перейти сюди
                            # F11 - зайти в multiply()
```

---

### 4. Variable Inspection (Інспекція змінних)

Під час паузи на breakpoint можна:

✅ **Переглянути значення змінних:**
- У панелі Variables (PyCharm)
- У панелі Watch (VS Code)

✅ **Побачити тип даних:**
```python
x = 42
# У панелі Variables:
# x: int = 42
```

✅ **Evaluate Expression (обчислити вираз):**
- PyCharm: Alt+F8
- VS Code: Debug Console

```python
x = 10
y = 5
# Evaluate: x + y * 2  → 20
```

---

### 5. Call Stack (Стек викликів)

Call Stack показує порядок викликів функцій:

```python
def function_c():
    result = 1 + 1  # 🔴 Breakpoint тут
    return result

def function_b():
    return function_c()

def function_a():
    return function_b()

function_a()
```

**Call Stack буде:**
```
function_c()    ← Поточна функція
function_b()    ← Викликана з function_b
function_a()    ← Викликана з function_a
<module>        ← Головний модуль
```

---

### 6. Watch Expressions (Вирази спостереження)

Додайте вираз для постійного спостереження:

```python
def calculate(x, y):
    result = x + y  # 🔴 Breakpoint
    return result * 2

# У Watch додайте:
# - x + y
# - result
# - type(result)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`
