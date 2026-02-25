# Lesson 1: Змінні та типи даних

## Теорія

### Змінні
Змінна - це контейнер для зберігання значень. На відміну від багатьох мов програмування, Python не потребує явного оголошення типу.

```python
name = "John"  # str
age = 25       # int
height = 5.9   # float
is_student = True  # bool
```

### Базові типи даних

#### Integer (int)
```python
age = 25
count = -10
binary = 0b1010  # 10 в двійковій системі
```

#### String (str)
```python
message = "Hello"
escaped = "He said \"Hello\""
multiline = """This is
a multiline
string"""
```

#### Float (float)
```python
price = 19.99
temperature = -5.5
pi = 3.14159
```

#### Boolean (bool)
```python
is_active = True
is_empty = False
```

### Перевірка типу

```python
value = 42
print(type(value))  # <class 'int'>
print(isinstance(value, int))  # True
```

## Приклади

Див. файл `examples/variables.py`

## Вправи

Виконайте завдання в папці `exercises/`

